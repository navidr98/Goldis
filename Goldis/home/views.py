from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home/index.html')

def services(request):
    return render(request, 'home/khadamat.html')

def about(request):
    return render(request, 'home/about.html')

def rules(request):
    return render(request, 'home/ghavanin.html')



