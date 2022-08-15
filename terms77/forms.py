from django import forms
from django.contrib.auth.models import User
from .models import companies, policies

class Update(forms.ModelForm):    
    class Meta:
        model = companies
        fields = ['company_name', 'business_platform', 'product_service', 'company_website']  

class Updates(forms.ModelForm):    
    class Meta:
        model = policies
        fields = ['company_names', 'business_platforms', 'product_services', 'company_websites']  