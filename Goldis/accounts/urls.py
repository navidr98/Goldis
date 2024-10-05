from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login-code/', views.login_sms)
]