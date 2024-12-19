from django.db import models
from django.db import models

# Create your models here.

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,default="Admin")
    email = models.EmailField(unique=True)
    psw = models.CharField(max_length=100)
    
    
    
class Login(models.Model):
    email = models.EmailField()
    psw = models.CharField(max_length=100)
    

class ImageUpload(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class CardsUpload(models.Model):
    title = models.CharField(max_length=100)
    Description = models.TextField()
    image = models.ImageField(upload_to='cards/',null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Enquiry(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.TextField()
    enquirydate=models.DateTimeField(auto_now_add=True)