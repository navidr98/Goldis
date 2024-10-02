from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegistrationForm(forms.Form):
    username = forms.CharField(label='نام کابری',)
    phone_number = forms.CharField(label='شماره تلفن',)
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput(attrs={'placeholder':'رمز عبور'}))
    confirm_password = forms.CharField(label='تکرار رمز عبور', widget=forms.PasswordInput(attrs={'placeholder':'تکرار رمز عبور'}))

    def clean(self):
        cd = super().clean()
        p1 = cd.get('password')
        p2 = cd.get('confirm_password')
        if p1 and p2 and p1 != p2:
            raise ValidationError('رمز عبور همخوانی ندارد')
