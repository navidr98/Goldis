from django import forms

class UserRegistrationForm(forms.Form):
    username = forms.CharField()
    phone_number = forms.IntegerField()
    password = forms.CharField()
    confirm_password = forms.CharField()
