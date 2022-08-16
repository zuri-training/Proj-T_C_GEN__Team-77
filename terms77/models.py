from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class companies(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    company_name = models.TextField(verbose_name="Company Name", max_length=50, null=True)
    business_platform = models.TextField(verbose_name="Business Platform", max_length=50, null=True)
    product_service = models.TextField(verbose_name="Product Service", max_length=50, null=True)
    company_website = models.TextField(verbose_name="Company Website", max_length=50, null=True)

    # def __str__(self):
    #     return self.user

class policies(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    company_names = models.TextField(verbose_name="Company Name", max_length=50, null=True)
    business_platforms = models.TextField(verbose_name="Business Platform", max_length=50, null=True)
    product_services = models.TextField(verbose_name="Product Service", max_length=50, null=True)
    company_websites = models.TextField(verbose_name="Company Website", max_length=50, null=True)

    # def __str__(self):
    #     return self.user
    




