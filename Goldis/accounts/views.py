from django.shortcuts import render, redirect
from django.views import View
from .forms import UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

def login_sms(request):


    return render(request , 'accounts/login.html')

class UserLoginView(View):

    form_class = UserLoginForm
    temp_name = 'accounts/login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.temp_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request,'با موفقیت وارد شدید', 'success')
                return redirect('home:home')
            messages.error(request, 'نام کابری یا رمز ورود اشتباه است', 'warning')
        return render(request, self.temp_name, {'form': form})
