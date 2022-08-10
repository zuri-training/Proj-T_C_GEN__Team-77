import email
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError

# from T_C_GEN.terms77.models import companies

# Create your views here.

def index(request):
    return render(request, 'index.html',{})

def signup(request):
    if request.method == 'POST':
        username = request.POST['fullname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already In Use')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('signin')
        else:
            messages.info(request, 'Password not the same.')
            return redirect('signup')
    else:
        return render(request, 'signup.html',{})

class EmailBackend(object):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect ('signin')

    else:
        return render(request, 'signin.html')

def dashboard(request):
    return render(request, 'dashboard.html',{})

def aboutus(request):
    return render(request, 'aboutus.html',{})

def forgotpass(request):
    return render(request, 'forgotpass.html',{})

def newterms(request):
    company_name = request.POST.["company_name"]
    business_platform = request.POST["business_platform"]
    product_service = request.POST["product_service"]
    companies = User.objects.create_user(company_name= company_name, business_platform=business_platform,product_service=product_service)
    companies.save();
    return render(request, 'newterms.html',{})
   
    
    

def ourprivacypolicy(request):
    return render(request, 'ourprivacypolicy.html',{})

def settings(request):
    return render(request, 'settings.html',{})

def termsofuse(request):
    return render(request, 'termsofuse.html',{})

# def step2(request):
#     return render(request, 'step2.html',{})

# def step3(request):
#     return render(request, 'step3.html',{})

def logout(request):
    auth.logout(request)
    return redirect('/')

def preview(request):
    return render(request, 'preview.html',{})

def dashboard_acct_edit(request):
    return render(request, 'dashboard-acct-edit.html',{})

def aboutus(request):
    return render(request, 'aboutus.html',{})

def faq(request):
    return render(request, 'faq.html',{})

def settingsedit(request):
    return render(request, 'settingsedit.html',{})


def step22(request):
    return render(request, 'step22.html',{})


def step33(request):
    return render(request, 'step33.html',{})


