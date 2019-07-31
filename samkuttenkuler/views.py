from django.views.generic import TemplateView
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .forms import contact_form
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect



class HomePage(TemplateView):
    template_name = "base.html"

class PortfolioPage(TemplateView):
    template_name = "portfolio.html"


def email(request):
    if request.method == 'GET':
        form = contact_form()
    else:
        form = contact_form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(name, message, email, ['sam.kuttenk@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')
    return render(request, "#Contact", {'form': form})

def thanks(request):
    return HttpResponse('Thank you for your message.')