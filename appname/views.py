from django.shortcuts import render,redirect
from .form import sponsorAddForm,sponsorForm,userForm,userAddForm
from django.contrib import messages, auth
from .models import UserDetail,SponsorDetail,SponsorShip,Feedback

# Create your views here.
def index(request):
    rev=Feedback.objects.all()
    context = {
        'rw':rev
        }
    return render(request, 'appname/index.html',context)

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

def feed(request):
    if request.method == 'POST':
        name=request.POST['name']
        message=request.POST['message']
        phone=request.POST['phone']
        email=request.POST['email']
        rev=Feedback.objects.create(uname =name,message=message,email=email,mobile_no=phone)
        rev.save()
        return redirect('/userboard')
    return render(request,'appname/feedback.html')

def seefeed(request):
    return render(request,'appname/seefeed.html')

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
    obj=UserDetail.objects.all()
    context={
    'obj':obj,
    }
    return render(request,'appname/spoboard.html',context)

def userboard(request):
   
    return render(request,'appname/userboard.html')
def sponsored(request):
   
    return render(request,'appname/sponsored.html')

def pay(request, patient=None, uaddress=None, umobile_no=None, ulocation=None):
    if request.method == 'POST':
        user = request.user
        patient = patient
        uaddress = uaddress
        umobile_no = umobile_no
        ulocation = ulocation
        card=request.POST['card']
        year=request.POST['year']
        cvv=request.POST['cvv']
        month=request.POST['month']
        amount=request.POST['amount']
        pay = SponsorShip.objects.create(cardnumber=card,year=year,cvv=cvv,month=month,amount=amount,sname=user.username,uname=patient, uaddress=uaddress, umobile_no=umobile_no, ulocation=ulocation)
        pay.save()
        return redirect('/sponsored')
    return render(request, 'appname/payment.html')



def logout(request):
    auth.logout(request)
    return redirect('/')


def about(request):
    user = request.user
    try:
        obj = UserDetail.objects.get(patient=user)
    except UserDetail.DoesNotExist:
        obj = None 

    context = {
        'obj': obj,
    }
    return render(request, 'appname/about.html', context)
