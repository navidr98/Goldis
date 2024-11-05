from django import forms
from .models import User, UserBankInfo
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# user model creation in django admin
class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('phone_number',)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError('password must match')
        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


# user model change information in django admin
class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField(help_text="you can change password via <a href=\"../password\">this form</a>")

    class Meta:
        model = User
        fields = ('phone_number', 'password', 'last_login')


# user register form shown in register page
class UserRegistrationForm(forms.Form):
    phone_number = forms.CharField(min_length=11, max_length=11, error_messages = {
                'required':"لطفا شماره تلفن خود را وارد کنید",
                'min_length': "شماره تلفن باید ۱۱ رقم باشد",
                'max_length': "شماره تلفن نباید بیشتر از ۱۱ رقم باشد",
                }, label='', widget=forms.TextInput(attrs={'placeholder':'شماره تلفن'}))

    password = forms.CharField(min_length=8, label='', error_messages = {
                 'required':"لطفا رمز عبور خود را وارد کنید",
                 'min_length': "رمز عبور باید حداقل ۸ حرف باشد",
                 }, widget=forms.PasswordInput(attrs={'placeholder':'رمز عبور'}))

    confirm_password = forms.CharField(min_length=8, label='', error_messages = {
                 'required':"لطفا رمز عبود خود را مجدد وارد کنید",
                 'min_length': "رمز عبور باید حداقل ۸ حرف باشد",
                 }, widget=forms.PasswordInput(attrs={'placeholder':'تکرار رمز عبور'}))

    def clean(self):
        cd = super().clean()
        p1 = cd.get('password')
        p2 = cd.get('confirm_password')
        if p1 and p2 and p1 != p2:
            raise ValidationError('رمز عبور همخوانی ندارد')

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        user = User.objects.filter(phone_number=phone_number).exists()
        if user:
            raise ValidationError('این شماره از قبل وجود دارد')
        return phone_number


# user login form shown in register page
class UserLoginForm(forms.Form):

    phone_number = forms.CharField(min_length=11, max_length=11, error_messages = {
                'required':"لطفا شماره تلفن خود را وارد کنید",
                'min_length': "شماره تلفن باید ۱۱ رقم باشد",
                'max_length': "شماره تلفن نباید بیشتر از ۱۱ رقم باشد",
                }, label='', widget=forms.TextInput(attrs={'placeholder':'شماره تلفن'}))

    password = forms.CharField(min_length=8, label='', error_messages = {
                 'required':"لطفا رمز عبور خود را وارد کنید",
                 'min_length': "رمز عبور باید حداقل ۸ حرف باشد",
                 }, widget=forms.PasswordInput(attrs={'placeholder':'رمز عبور'}))

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        user = User.objects.filter(phone_number=phone_number).exists()
        if not user:
            raise ValidationError('شماره تلفن یا رمز عبور اشتباه است')
        return phone_number


#sms code verification in user register form
class VerifyCodeForm(forms.Form):
    code = forms.IntegerField(label='', error_messages = {
                'required':"لطفا کد ارسال شده را وارد کنید",
                'min_length': "کد باید ۴ رقم باشد",
                'max_length': "کد باید ۴ رقم باشد",
                'invalid':"لطفا کد با فرمت صحیح وارد کنید"},
                widget=forms.TextInput(attrs={'placeholder':'کد یکبار مصرف'}))


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('phone_number', 'full_name')

        widgets = {
            'phone_number': forms.TextInput(attrs={'placeholder': 'شماره تلفن'}),
            'full_name': forms.TextInput(attrs={'placeholder': 'نام و نام خانوادگی '}),
        }
        labels = {
            'phone_number': '',
            'full_name': '',
        }
        error_messages = {
            'phone_number': {
                'required': 'لطفا شماره تلفن همراه را وارد کنید',
                'invalid': 'شماره همراه نمی تواند خالی باشد',
                'min_length': "شماره تلفن باید ۱۱ رقم باشد",
                'max_length': "شماره تلفن باید ۱۱ رقم باشد",
            },
            'full_name': {
                'required': 'نام و نام خانوادگی را وارد کنید',
                'invalid': 'نام و نام خانو',
                'max_length': "نام و نام خانوادگی باید کمتر از ۱۰۰ حرف باشد",
            },
        }

class UserChangePasswordForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('password',)
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'رمز عبور'})
        }
        labels = {
            'password': '',
        }
        error_messages = {
            'password': {
                'required': "لطفا رمز عبود خود را مجدد وارد کنید",
                'min_length': "رمز عبور باید حداقل ۸ حرف باشد",
            },
        }

    confirm_password = forms.CharField(min_length=8, label='', error_messages={
        'required': "لطفا رمز عبود خود را مجدد وارد کنید",
        'min_length': "رمز عبور باید حداقل ۸ حرف باشد",
    }, widget=forms.PasswordInput(attrs={'placeholder': 'تکرار رمز عبور'}))

    def clean(self):
        cd = super().clean()
        p1 = cd.get('password')
        p2 = cd.get('confirm_password')
        if p1 and p2 and p1 != p2:
            raise ValidationError('رمز عبور همخوانی ندارد')

class UserBankInfoForm(forms.ModelForm):
    class Meta:
        model = UserBankInfo
        fields = ('cart_no', 'sheba')

    widgets = {
        'cart_no': forms.TextInput(attrs={'placeholder': 'شماره کارت'}),
        'sheba': forms.TextInput(attrs={'placeholder': 'شماره شبا'}),
    }
    labels = {
        'cart_no': '',
        'sheba': '',
    }
    error_messages = {
        'cart_no': {
            'required':"شماره کارت را وارد کنید",
            'invalid':"شماره کارت را با فرمت صحیح وارد کنید"
        },
        'sheba': {
            'required':"شماره شبا را وارد کنید",
            'invalid':"شماره شبات را با فرمت صحیح وارد کنید"
        },
    }
