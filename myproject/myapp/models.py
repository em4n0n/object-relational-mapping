from django.db import models

# Create your models here.
class Customer(models.Model): 
    name = models.CharField(max_length=255) 

class Vehicle(models.Model): 
    name = models.CharField(max_length=255) 
    model = models.CharField(max_length=100)
    customer = models.ForeignKey( 
        Customer, 
        on_delete=models.CASCADE, 
        related_name='Vehicle' 
    ) 