from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

from .models import Users
from .models import Companies
from .models import company_policies
from .models import company_policy_contacts

# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Users)
admin.site.register(Companies)
admin.site.register(company_policies)
admin.site.register(company_policy_contacts)
