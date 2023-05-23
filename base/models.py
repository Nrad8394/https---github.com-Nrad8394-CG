# from click import Group
from django.db import models
import uuid
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.




class CustomUser(AbstractUser):
    pass

    


class Item(models.Model):
    item_name = models.CharField(max_length=100)
    specification = models.TextField()
    
    item_status = models.CharField(max_length=255 , null=True, blank=True)
    item_id = models.CharField(max_length=32,primary_key=True, unique=True)
    def save(self, *args, **kwargs):
        if not self.item_id:
            self.item_id = uuid.uuid4().hex[:8]  # Generate a unique 8-character code
        super().save(*args, **kwargs)
        objects = models.Manager()

    def __str__(self):
        return self.item_name

class Transporter(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    transporter_name = models.CharField(max_length=255,null=True)
    transporter_email_address = models.CharField(max_length=255, null=True)
    transporter_phone_number = models.IntegerField(default=0)
    transporter_address = models.TextField(null=True)
    objects = models.Manager()

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    item_id = models.ForeignKey(Item, on_delete= models.CASCADE, null=True, default=None)
    transporter_id = models.ForeignKey(Transporter, on_delete=models.CASCADE, null=True, default=None)    
    # transporter_name = models.CharField(max_length=255, null=True) 
    destination = models.CharField(max_length=100)
    receiver_first_name = models.CharField(max_length=255)
    receiver_last_name = models.CharField(max_length=255)
    receiver_phone_number = models.IntegerField(null=True)
    receiver_confirmation = models.BooleanField( null=True)
    objects = models.Manager()
    item_status = models.CharField(max_length=255)



    unique_code = models.CharField(max_length=32, unique=True)

    def save(self, *args, **kwargs):
        if not self.unique_code:
            self.unique_code = uuid.uuid4().hex[:8]  # Generate a unique 8-character code
        super().save(*args, **kwargs)
    

           