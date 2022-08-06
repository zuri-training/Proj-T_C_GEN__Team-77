from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.
class Users(models.Model):
    Fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.TextField(max_length=50)

    def __str__(self):
        return self.Fullname


class Companies(models.Model):
    user_id = models.IntegerField()
    company_name = models.ForeignKey(Users, on_delete=models.CASCADE)
    company_address = models.TextField(max_length=50)
    country = models.TextField(max_length=50)

    def __str__(self):
        return self.user_id


class company_policies(models.Model):
    company_id = models.IntegerField()
    uses_personal_info = models.BooleanField()
    uses_user_acct = models.BooleanField()
    uses_third_party_services = models.BooleanField()
    uses_newsletter = models.BooleanField()
    uses_user_upload_images = models.BooleanField()
    uses_underage = models.BooleanField()
    uses_ads = models.BooleanField()
    uses_customer_data = models.BooleanField()
    uses_retargeting_advertising = models.BooleanField()
    uses_money = models.BooleanField()
    promoted_company = models.BooleanField()

    def __str__(self):
        return self.company_id


class company_policy_contacts(models.Model):
    company_id = models.IntegerField()
    uses_email = models.BooleanField()
    uses_website = models.BooleanField()

    def __str__(self):
        return self.company_id


class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    objects = CustomUserManager()
