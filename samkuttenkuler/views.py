from django.views.generic import TemplateView
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .forms import contact_form
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import redirect


class HomePage(TemplateView):
    template_name = "base.html"

class PortfolioPage(TemplateView):
    template_name = "portfolio.html"


    def POST(self, request):
        if request.method == 'GET':
            form = contact_form()
        else:
            form = contact_form(request.POST)
            if form.is_valid():
                contact_name = form.cleaned_data['contact_name']
                contact_email = form.cleaned_data['contact_email']
                contact_message = form.cleaned_data['contact_message']
                try:
                    send_mail(contact_name, contact_email, contact_message, ['sam.kuttenk@gmail.com'])
                except BadHeaderError:
                    return HttpResponse('Invalid header...')
                return redirect('success')
        return render(request, self.template_name, {'form':form})

    def success(request):
        return HttpResponse('Thank you!')

