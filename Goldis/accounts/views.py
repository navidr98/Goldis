from pyexpat.errors import codes, messages
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationForm, VerifyCodeForm
import random
from utils import send_otp_code
from .models import OtpCode, User
from django.contrib import messages


class UserRegisterView(View):

    form_class = UserRegistrationForm

    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/register.html', {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(1000,9999)
            send_otp_code(form.cleaned_data['phone_number'], random_code)
            OtpCode.objects.create(phone_number=form.cleaned_data['phone_number'], code=random_code)
            request.session['user_registration_info'] = {
                'phone_number':form.cleaned_data['phone_number'],
                'email':form.cleaned_data['email'],
                'password':form.cleaned_data['password'],
            }
            messages.success(request,'We sent you a code', 'success')
            return redirect('accounts:verify_code')
        return redirect('home:home')


class UserRegisterVerifyCodeView(View):

    form_class = VerifyCodeForm

    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/verify.html', {'form':form})


    def post(self, request):
        user_session = request.session['user_registration_info']
        code_instance = OtpCode.objects.get(phone_number=user_session['phone_number'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['code']  == code_instance:
                User.objects.create_user(user_session['phone_number'], user_session['email'], user_session['password'])
                code_instance.delete()
                messages.success(request, 'You registered', 'success')
                return redirect('home:home')
            else:
                messages.error(request, 'You registered', 'error')
                return redirect('accounts:verify_code')
        return render(request, 'accounts/verify.html', {'form': form})