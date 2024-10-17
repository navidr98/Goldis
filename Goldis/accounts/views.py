from django.shortcuts import render, redirect
from django.views import View
from .forms import UserLoginForm
from .forms import UserRegistrationForm

from django.contrib import messages
from django.contrib.auth import authenticate, login

from django.contrib.auth import authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Account
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

class UserRegisterView(View):
    form_class = UserRegistrationForm
    tamp_name = 'accounts/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.tamp_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            account = Account(
                phone_number=cd['phone_number'],
                password=make_password(cd['password']),  # Hash the password
                rial_balance='0',
                gold_balance='0'
            )
            account.save()
            messages.success(request, 'ثبت نام شما با موفقیت انجام شد', 'success')
            return redirect('home:home')
        return render(request, self.tamp_name, {'form': form})

class UserLoginView(View):
    form_class = UserLoginForm
    temp_name = 'accounts/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.temp_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                user = Account.objects.get(phone_number=cd['phone_number'])
            except Account.DoesNotExist:
                user = None

            if user and check_password(cd['password'], user.password):
                request.session['user_id'] = user.User_ID
                request.session['phone_number'] = user.phone_number
                messages.success(request,'با موفقیت وارد شدید', 'success')
                return redirect('home:home')
            else:
                messages.error(request, 'نام کابری یا رمز ورود اشتباه است', 'warning')
        return render(request, self.temp_name, {'form': form})

class UserLogoutView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'

    def get(self, request):
        logout(request)
        messages.success(request, 'با موفقیت از حساب خود خارج شدید', 'success')
        return redirect('home:home')