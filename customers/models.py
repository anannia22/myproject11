from django.db import models

# Model for customer
from django.contrib.auth.models import User
class customer (models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    name=models.CharField(max_length=200)
    address=models.TextField()
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_image=models.ImageField(upload_to='media/')
    

    #priority=models.IntegerChoices(default=0)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    create_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
 
    def __str__(self):
        return self.title
    

# Create your models here.
class Priority(models.IntegerChoices):
    LOW = 0, 'Low'
    MEDIUM = 1, 'Medium'
    HIGH = 2, 'High'

priority = models.IntegerField(choices=Priority.choices, default=Priority.LOW)

