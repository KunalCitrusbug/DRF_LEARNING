from django.contrib.auth.models import User
from django.db import models


# BRAND
class Brand(models.Model):
    brand = models.CharField(max_length=100,)


# PRODUCTS
class Mail(models.Model):
    subject = models.CharField(max_length=100)
    mail_to = models.CharField(max_length=100)
    body = models.TextField()

