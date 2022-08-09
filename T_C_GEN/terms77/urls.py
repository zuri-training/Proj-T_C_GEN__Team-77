from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup"),
    # path("admin/", admin.site.urls),
    
]

