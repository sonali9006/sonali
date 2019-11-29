from django.db import models

class MerchantModel(models.Model):
    Merchant_Id = models.IntegerField(primary_key=True)
    Merchant_Name = models.CharField(max_length=30)
    Merchant_Contact = models.IntegerField(unique=True)
    Merchant_Email = models.EmailField(unique=True)
    Merchant_Password = models.CharField(max_length=60)
