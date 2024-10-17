from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserLoginForm(forms.Form):
    phone_number = forms.CharField(min_length=11, max_length=11, error_messages = {
                'required':"لطفا شماره تلفن خود را وارد کنید"},
                label='', widget=forms.TextInput(attrs={'placeholder':'شماره تلفن', 'class':''}))
    password = forms.CharField(min_length=8, label='', error_messages = {
                 'required':"لطفا رمز عبور خود را وارد کنید"
                 }, widget=forms.PasswordInput(attrs={'placeholder':'رمز عبور', 'class':''}))
    
from django.core.exceptions import ValidationError

class UserRegistrationForm(forms.Form):
    phone_number = forms.CharField(min_length=11, max_length=11, error_messages = {
                'required':"لطفا شماره تلفن خود را وارد کنید",
                'min_length': "شماره تلفن باید ۱۱ رقم باشد",
                'max_length': "شماره تلفن نباید بیشتر از ۱۱ رقم باشد",
                }, label='', widget=forms.TextInput(attrs={'placeholder':'شماره تلفن', 'class':''}))
    password = forms.CharField(min_length=8, label='', error_messages = {
                 'required':"لطفا رمز عبور خود را وارد کنید",
                 'min_length': "رمز عبور باید حداقل ۸ حرف باشد",
                 }, widget=forms.PasswordInput(attrs={'placeholder':'رمز عبور', 'class':''}))
    confirm_password = forms.CharField(min_length=8, label='', error_messages = {
                 'required':"لطفا رمز عبود خود را مجدد وارد کنید",
                 'min_length': "رمز عبور باید حداقل ۸ حرف باشد",
                 }, widget=forms.PasswordInput(attrs={'placeholder':'تکرار رمز عبور', 'class':''}))

    def clean(self):
        cd = super().clean()
        p1 = cd.get('password')
        p2 = cd.get('confirm_password')
        if p1 and p2 and p1 != p2:
            raise ValidationError('رمز عبور همخوانی ندارد')
