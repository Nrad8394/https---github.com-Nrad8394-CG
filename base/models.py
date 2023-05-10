from django.db import models 
import uuid

# Create your models here.
class items(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    item_unique_code = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)


    def __str__(self):
        return self.name
    
class transfer(models.Model):
    item = models.ForeignKey(items, on_delete=models.CASCADE)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    transfer_status = models.CharField(max_length=100)
    unique_code = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    # def __str__(self):
    #     return f"{self.item} - {self.transfer_status}"
