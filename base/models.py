# from click import Group
from django.db import models
import uuid
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.




class CustomUser(AbstractUser):
    user_type_choice = ((1,'Admin'),(2,'Clerk'),(3,'Customer'))
    user_type = models.CharField(default=1, choices=user_type_choice ,max_length = 1)
    
    pass
 
 
class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    
class Clerk(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_model = models.CharField(max_length=100, default=None)
    specification = models.TextField()
    serial_number = models.CharField(max_length=100, null=True)
    item_status = models.CharField(max_length=255 , default=None)
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
    
#Creating Django Signals

# It's like trigger in database. It will run only when Data is Added in CustomUser model

@receiver(post_save, sender=CustomUser)
# Now Creating a Function which will automatically insert data in AdminManager, Clerk or Supplier
def create_user_profile(sender, instance, created, **kwargs):
    # if Created is true (Means Data Inserted)
    if created:
        # Check the user_type and insert the data in respective tables
        if instance.user_type == 1:
            Admin.objects.create(user=instance)
        if instance.user_type == 2:
            Clerk.objects.create(user=instance)
        if instance.user_type == 3:
            Customer.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.admin.save()
    if instance.user_type == 2:
        instance.clerk.save()
    if instance.user_type == 3:
        instance.customer.save()
    


           