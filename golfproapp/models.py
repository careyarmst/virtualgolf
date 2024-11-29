from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
import datetime

# Create your models here.

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    is_golfer = models.BooleanField(default=False)
    fname = models.TextField(default="Golfer1")
    lname = models.TextField(default="Golfer1Lname")
    g_phone = models.CharField(default="55-867-5309", max_length=15)
    g_email = models.CharField(default="bob.smith@aol.com", max_length=30)

def __str__(self):
    return self.customer_id

class inv_options(models.Model):
    opt_name = models.CharField(default="Tees", max_length=50)

def __str__(self):  
    return self.opt_name

class inventory(models.Model):
    inv_id = models.IntegerField(default=1)
    inv_options = models.ForeignKey(inv_options, on_delete=models.CASCADE)
    inv_description = models.CharField(default="Hat",max_length=255)
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)

def __str__(self):
    return self.inv_id

class order(models.Model):
    products = models.ManyToManyField(inventory, through="OrderItem")
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.products

class OrderItem(models.Model):
    order = models.ForeignKey(order, on_delete=models.CASCADE)
    inventory = models.ForeignKey(inventory, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class Golfing(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    tee_time = models.DateTimeField(default=datetime.datetime(2024,11,24,23,59,59))
    no_in_party = models.PositiveIntegerField(default=4)
    avg_grp_hcp = models.PositiveIntegerField(default=26)
                                    
class Purchase(models.Model):
    subtotal = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    tax = models.DecimalField(decimal_places=2, max_digits=2, default=.05)
    total = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)

