from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class contact_form(forms.Form):
    contact_name = forms.CharField(label='Name', max_length=255)
    contact_email = forms.CharField(label='Email',max_length=255)
    contact_message = forms.CharField(required=True, widget=forms.Textarea)

