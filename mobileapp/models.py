from django.db import models
from django.utils import timezone
# Create your models here.
colors = [
    ('Black','Black'),
    ('White','White'),
    ('Silver','Silver'),
]

class Mobile(models.Model):
    Customer_name=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    Email=models.EmailField(default="@gmail.com")
    Brand=models.CharField(max_length=100,default="Mi11x")
    Color=models.CharField(max_length=100,choices=colors)
    Contact=models.IntegerField()
    Ordered_Date=models.DateTimeField(auto_now=True,null=True) 
    Price=models.IntegerField()
    def __str__(self):
        return self.Customer_name