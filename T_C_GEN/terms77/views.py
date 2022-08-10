from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import company_policies, Users, Companies, company_policy_contacts

# Create your views here.
