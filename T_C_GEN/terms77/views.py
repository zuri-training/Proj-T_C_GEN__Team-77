from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import companies, policies
from django.db import models
from django.conf import settings
from .forms import Update, Updates


from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    return render(request, "index.html", {})


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        fullname = request.POST["fullname"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already In Use")
                return redirect("signup")
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password
                )
                user.save()
                return redirect("signin")
        else:
            messages.info(request, "Password not the same.")
            return redirect("signup")
    else:
        return render(request, "signup.html", {})


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
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid Credentials")
            return redirect("signin")

    else:
        return render(request, "signin.html")


def dashboard(request):
    return render(request, "dashboard.html", {})


def aboutus(request):
    return render(request, "aboutus.html", {})


def forgotpass(request):
    return render(request, "forgotpass.html", {})


def newterms(request):
    if request.method == "POST":
        user = models.ForeignKey(user, on_delete=models.CASCADE, blank=True, null=True)
        company_name = request.POST["company_name"]
        business_platform = request.POST["business_platform"]
        product_service = request.POST["product_service"]
        company_website = request.POST["company_website"]
        data = companies(
            company_name=company_name,
            business_platform=business_platform,
            product_service=product_service,
            company_website=company_website,
        )
        data.save()

        if company_name is not None:
            return render(request, "ready.html", {})
        else:
            return render(request, "newterms.html", {})
    else:
        return render(request, "newterms.html", {})


def privacypolicynt(request):
    if request.method == "POST":
        # users = models.ForeignKey(
        #     users, on_delete=models.CASCADE, blank=True, null=True
        # )
        company_names = request.POST["company_names"]
        business_platforms = request.POST["business_platforms"]
        product_services = request.POST["product_services"]
        company_websites = request.POST["company_websites"]
        data = policies(
            company_names=company_names,
            business_platforms=business_platforms,
            product_services=product_services,
            company_websites=company_websites,
        )
        data.save()

        if company_names is not None:
            return render(request, "ready2.html", {})
        else:
            return render(request, "privacypolicynt.html", {})
    else:
        return render(request, "privacypolicynt.html", {})


def ourprivacypolicy(request):
    return render(request, "ourprivacypolicy.html", {})


def settings(request):
    return render(request, "settings.html", {})


def termsofuse(request):
    return render(request, "termsofuse.html", {})


def step2(request):
    return render(request, "step2.html", {})


def step3(request):
    return render(request, "step3.html", {})


def logout(request):
    auth.logout(request)
    return redirect("index")


def preview(request):
    data = companies.objects.all().values(
        "company_name", "business_platform", "product_service"
    )
    context = {"data": data}
    return render(request, "preview.html", context)


def preview2(request):
    datas = policies.objects.all().values(
        "company_names", "business_platforms", "product_services"
    )
    context = {"datas": datas}
    return render(request, "preview2.html", context)


@login_required
def dashboard_acct_edit(request):
    # if request.method == 'POST':
    #     user_form = UpdateUserForm(request.POST, instance=request.user)

    #     if user_form.is_valid():
    #         user_form.save()
    #         return redirect(to='settings')
    # else:
    #     user_form = UpdateUserForm(instance=request.user)

    return render(request, "dashboard-acct-edit.html", {})


def aboutus(request):
    return render(request, "aboutus.html", {})


def faq(request):
    return render(request, "faq.html", {})


def settingsedit(request):
    return render(request, "settingsedit.html", {})


def step22(request):
    return render(request, "step22.html", {})


def step33(request):
    return render(request, "step33.html", {})


def contactus(request):
    return render(request, "contactus.html", {})
