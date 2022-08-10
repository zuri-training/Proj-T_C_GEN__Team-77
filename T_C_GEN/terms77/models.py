from django.db import models

# Create your models here.

class companies(models.Model):
    user_id = models.IntegerField()
    company_name = models.TextField(max_length=50)
    business_platform = models.TextField(max_length=50)
    product_service = models.TextField(max_length=50)
    company_website = models.TextField(max_length=50)

    def __str__(self):
        return self.user_id




