from django.db import models

# Create your models here.

class User_info(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    vehicle_number = models.CharField(max_length=50, unique=True)
    vehicle_type = models.CharField(max_length=200)
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=51)
    class Meta:
        db_table="backend_user"
        
    def __str__(self,*args, **kwargs):
        return self.name

class feedback(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    review = models.TextField()
    class Meta:
        db_table="backend_feedback"