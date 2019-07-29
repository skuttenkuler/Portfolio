from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail, BadHeaderError
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail('New Enquiry', message, sender_email, ['sam.kuttenk@gmail.com'])

            return HttpResponse('Thank you!')

        else:
            form = ContactForm()


        return render(request,'samkuttenkuler/templates/portfolio.html', {'form':form})