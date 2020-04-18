from .models import *
from django import forms
from django.contrib.auth.hashers import make_password


class AdminForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', 'password', 'phone_number', 'email','first_name','last_name','age']


        widgets = {

            'username': forms.TextInput(attrs={
                'class': 'form-control',

            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',

            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',

            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',

            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',

            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',

            }),
            'age': forms.TextInput(attrs={
                'class': 'form-control',

            }),
        }

    def clean_password(self):
        return make_password(self.cleaned_data['password'])
