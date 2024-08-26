from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'appname/index.html')

def test(request):
    return render(request,'appname/test.html')

def login(request):
    return render(request,'appname/login.html')

def regspo(request):
    return render(request,'appname/regspo.html')

def regus(request):
    return render(request,'appname/regus.html')

def spoboard(request):
    return render(request,'appname/spoboard.html')

def userboard(request):
    return render(request,'appname/userboard.html')