from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from . import forms 
from django.views.generic import CreateView


# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreationForm
    template_name = 'signup.html '