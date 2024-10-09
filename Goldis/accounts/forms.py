from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserLoginForm(forms.Form):
    username = forms.CharField(min_length=5, label='', error_messages = {
                 'required':"لطفا نام کاربری خود را وارد کنید"
                 }, widget=forms.TextInput(attrs={'placeholder':'نام کاربری', 'class':''}))
    password = forms.CharField(min_length=8, label='', error_messages = {
                 'required':"لطفا رمز عبور خود را وارد کنید"
                 }, widget=forms.PasswordInput(attrs={'placeholder':'رمز عبور', 'class':''}))