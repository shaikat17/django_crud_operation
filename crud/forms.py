from django.core import validators
from django import forms
from django.shortcuts import render
from .models import User

class UserRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'mobile_no', 'email', 'password']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'mobile_no' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
        }