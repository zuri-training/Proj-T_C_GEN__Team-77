from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class companies(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.TextField(max_length=50, default="")
    business_platform = models.TextField(max_length=50, default="")
    product_service = models.TextField(max_length=50, default="")
    company_website = models.TextField(max_length=50, default="")

    # def __str__(self):
    #     return self.company_name

class policies(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_names = models.TextField(max_length=50, default="")
    business_platforms = models.TextField(max_length=50, default="")
    product_services = models.TextField(max_length=50, default="")
    company_websites = models.TextField(max_length=50, default="")

    # def __str__(self):
    #     return self.company_names
    




