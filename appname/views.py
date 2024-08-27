from django.shortcuts import render,redirect
from .form import sponsorAddForm,sponsorForm,userForm,userAddForm
from django.contrib import messages, auth
from .models import UserDetail,SponsorDetail,SponsorShip

# Create your views here.
def index(request):
    return render(request, 'appname/index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            try:
                if UserDetail.objects.filter(patient=user).exists():
                    return redirect('user_dashboard')
                elif SponsorDetail.objects.filter(sponsor=user).exists():
                    return redirect('sponsor_dashboard')
                else:
                    messages.info(request, "User type is not recognized.")
                    return redirect('appname/login.html')
            except Exception as e:
                messages.error(request, f"An error occurred: {str(e)}")
                return redirect('appname/login.html')
        else:
            messages.info(request, "Invalid login details!")
            return redirect('appname/login.html')
    
    return render(request, "appname/login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def test(request):
    return render(request,'appname/test.html')

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



