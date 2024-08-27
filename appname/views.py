from django.shortcuts import render
from .form import sponsorAddForm,sponsorForm

# Create your views here.
def index(request):
    return render(request, 'appname/index.html')

def test(request):
    return render(request,'appname/test.html')

def login(request):
    return render(request,'appname/login.html')

def regspo(request):
    registered = False
    if request.method == 'POST':
        var_sponsorForm = sponsorForm(request.POST)
        var_sponsorAddForm = sponsorAddForm(request.POST)
        if var_sponsorForm.is_valid() and var_sponsorAddForm.is_valid():
            sponsorprimary = var_sponsorForm.save()
            sponsorprimary.set_password(sponsorprimary.password)
            sponsorprimary.save()
            sponsorAdd = var_sponsorAddForm.save(commit=False)
            sponsorAdd.sponsor = sponsorprimary
            sponsorAdd.save()
            registered = True
    else:
        var_sponsorForm = sponsorForm()
        var_sponsorAddForm = sponsorAddForm()
    return render(request,'appname/regspo.html', {'var_sponsorForm': var_sponsorForm, 'var_sponsorAddForm': var_sponsorAddForm, 'registered': registered})

def regus(request):
    return render(request,'appname/regus.html')

def spoboard(request):
    return render(request,'appname/spoboard.html')

def userboard(request):
    return render(request,'appname/userboard.html')

