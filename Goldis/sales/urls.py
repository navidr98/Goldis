from django.urls import path
from . import views

app_name = 'sales'

urlpatterns = [
    #path('', views.index, name='index'),
    #path('sales/', views.sales_list, name='sales_list'),
    path('buy/', views.buy, name='buy'),
    path('sell/', views.sell, name='sell'),
    path('buyfactor/', views.buyfactor, name='buyfactor'),
    path('sellfactor/', views.sellfactor, name='sellfactor'),
    path('wallet/' , views.wallet_view , name = 'wallet'),
    path('deposit/' , views.deposit , name = 'deposit'),
    path('withdraw/' , views.withdraw , name = 'withdraw'),
    path('transactions/' , views.transactions , name = 'transactions'),

]

