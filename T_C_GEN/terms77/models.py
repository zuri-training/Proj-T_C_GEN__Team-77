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
    username = models.TextField(max_length=50)
    country = models.TextField(max_length=50)
    business_platform = models.TextField(max_length=50)
    product_service = models.TextField(max_length=50)
    website_name = models.TextField(max_length=50)

    def __str__(self):
        return self.user_id


class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    objects = CustomUserManager()
