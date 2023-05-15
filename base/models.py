# from click import Group
from django.db import models
import uuid
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.



class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(email, username, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
   




class Item(models.Model):
    id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=100)
    specification = models.TextField()
    item_id = models.IntegerField(null=True, blank=True,unique=True)
    objects = models.Manager()

    def __str__(self):
        return self.item_name

class Transporter(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    phone_number = models.IntegerField(default=0)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    objects = models.Manager()

    
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    item_id = models.ForeignKey(Item, on_delete= models.CASCADE, default=1)
    destination = models.CharField(max_length=100)
    transporter_id = models.ForeignKey(CustomUser, on_delete= models.CASCADE, default=1)
    receiver_first_name = models.CharField(max_length=255)
    receiver_last_name = models.CharField(max_length=255)
    receiver_id_number = models.IntegerField(default=0)
    receiver_confirmation = models.BooleanField(default=False, null=True)
    objects = models.Manager()
    unique_code = models.CharField(max_length=32, unique=True,default=0)

    def save(self, *args, **kwargs):
        if not self.unique_code:
            self.unique_code = uuid.uuid4().hex[:8]  # Generate a unique 8-character code
        super().save(*args, **kwargs)
    
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    # if Created is true (Means Data Inserted)
    if created: 
        Transporter.objects.create(user=instance)
@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.transporter.save()
           