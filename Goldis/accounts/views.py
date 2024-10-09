from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin

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
            User.objects.create_user(cd['username'],cd['phone_number'], cd['password'])
            messages.success(request, 'ثبت نام شما با موفقیت انجام شد', 'success')
            return redirect('home:home')
        return render(request, self.tamp_name, {'form': form})

class UserLogoutView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'

    def get(self, request):
        logout(request)
        messages.success(request, 'با موفقیت از حساب خود خارج شدید', 'success')
        return redirect('home:home')