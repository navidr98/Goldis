from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('rules/', views.rules, name='rules'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),

]