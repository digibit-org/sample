from django.db import models

# Create your models here.
# class Contact(models.Model):
#     name = models.CharField(max_Length=30)
#     email = models.EmailField()
#     message = models.TextField()

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()

class Register(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.TextField()

class Login(models.Model):
    email = models.EmailField()
    phone = models.TextField()