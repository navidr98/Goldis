from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        'current_page' : 'home',
    }
    return render(request, 'home/index.html', context)

def services(request):
    return render(request, 'home/khadamat.html')

def about(request):
    return render(request, 'home/about.html')

def rules(request):
    return render(request, 'home/ghavanin.html')




