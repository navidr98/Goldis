from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html')

def notfound(request):
    return render(request, 'home/Error404.html')

def badreq(request):
    return render(request, 'home/Error400.html')

def permission(request):
    return render(request, 'home/Error403.html')

def serverissue(request):
    return render(request, 'home/Error500.html')
