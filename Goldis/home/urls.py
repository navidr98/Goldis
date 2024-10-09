from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('404', views.notfound, name='Error404'),
    path('400', views.badreq, name='Error400'),
    path('403', views.permission, name='Error403'),
    path('500', views.serverissue, name='Error500'),
]

