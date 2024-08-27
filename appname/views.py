from django.shortcuts import render
from .form import sponsorAddForm,sponsorForm,userForm,userAddForm

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
    registered = False
    if request.method == 'POST':
        var_userForm = userForm(request.POST, request.FILES)
        var_userAddForm = userAddForm(request.POST, request.FILES)
        if var_userForm.is_valid() and var_userAddForm.is_valid():
            userprimary = var_userForm.save()
            userprimary.set_password(userprimary.password)
            userprimary.save()
            userAdd = var_userAddForm.save(commit=False)
            userAdd.patient = userprimary
            if 'img' in request.FILES:
                userAdd.img = request.FILES['img']
            userAdd.save()
            registered = True
    else:
        var_userForm = userForm()
        var_userAddForm = userAddForm()
    return render(request,'appname/regus.html', {
        'var_userForm': var_userForm,
        'var_userAddForm': var_userAddForm,
        'registered': registered
    })

def spoboard(request):
    return render(request,'appname/spoboard.html')

def userboard(request):
    return render(request,'appname/userboard.html')


