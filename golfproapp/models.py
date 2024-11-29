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

class Misc_purchases(models.Model):
    inv_id = models.IntegerField(default=1)
    inv_description = models.CharField(default="Hat",max_length=255)
    misc_quantity = models.IntegerField(default=1)
    misc_price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    misc_subtotal = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    misc_tax=models.DecimalField(default=.05, max_digits=10, decimal_places=2)
    misc_total=models.DecimalField(default=.05, max_digits=10, decimal_places=2)

def __str__(self):
    return self.inv_id

class Golf_Data(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    tee_time = models.DateTimeField(default=datetime.datetime(2024,11,24,23,59,59))
    no_in_party = models.PositiveIntegerField(default=4)
    avg_grp_hcp = models.PositiveIntegerField(default=26)

def __str__(self):
    return self.customer_id


class Golf_purchases(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    holes_18_price = models.DecimalField(default=35.00, max_digits=10, decimal_places=2)
    holes_9_price = models.DecimalField(default=20.00, max_digits=10, decimal_places=2)
    cart_9_price = models.DecimalField(default=9.00, max_digits=10, decimal_places=2)
    cart_18_price = models.DecimalField(default=12.00, max_digits=10, decimal_places=2)
    golf_subtotal = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    golf_tax=models.DecimalField(default=.05, max_digits=10, decimal_places=2)
    golf_total=models.DecimalField(default=.05, max_digits=10, decimal_places=2)

def __str__(self):
    return self.customer_id
