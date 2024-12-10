# Create your models here.
from django.db import models
import datetime
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver


# Create your models here.

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    golferchoice=[('Y','Yes'),('N','No'),]
    gchoice = models.CharField(max_length=1, choices=golferchoice, default='Y')
    fname = models.TextField(max_length=10, default="Golfer1")
    lname = models.TextField(max_length=10, default="Golfer1Lname")
    g_phone = models.CharField(default="555-867-5309", max_length=15)
    g_email = models.CharField(default="bob.smith@aol.com", max_length=30)

def __str__(self):
    return self.Customer.customer_id

class Misc_purchases(models.Model):
    mp_date = models.DateField(default=timezone.now)
    purch_id = models.IntegerField(default=1)
    inv_id = models.IntegerField(default=1)
    inv_description = models.CharField(default="Hat",max_length=255)
    inv_choices = [
                  ('TE','Tees'),
                  ('PH','Premium Hat'),
                  ('RH','Regular Hat'), 
                  ('DOZ','Dozen Golf Balls'), 
                  ('SL','Sleeve Golf Balls'), 
                  ('IND','Individual Golf Ball'), 
                  ('CR', 'Club Rental'),
                  ('OTH','Other')
                  ]
    ichoice = models.TextField(max_length=50, choices=inv_choices, default=('RH','Regular Hat'))
    misc_quantity = models.IntegerField(default=1)
    misc_price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    misc_subtotal = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    misc_tax=models.DecimalField(default=.05, max_digits=10, decimal_places=2)
    misc_total=models.DecimalField(default=.05, max_digits=10, decimal_places=2)

    def save(self,*args,**kwargs):
        self.misc_subtotal=float(self.misc_quantity*self.misc_price)
        self.misc_tax=float(self.misc_quantity+self.misc_price)*.05
        self.misc_total=float(self.misc_subtotal+self.misc_tax)
        super().save(*args, **kwargs)
  
def __str__(self):
    return self.purch_id

class Golf_Data(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    golf_date = models.DateField(default='2024-11-24')
    tee_time = models.DateTimeField(default=datetime.datetime(2024,11,24,23,59,59))
    no_in_party = models.PositiveIntegerField(default=4)
    avg_grp_hcp = models.PositiveIntegerField(default=26)

def __str__(self):
    return self.customer_id

class Golf_purchases(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    gp_date= models.DateField(default=timezone.now)
    gp_id = models.IntegerField(default=1, unique=True)
    num_18_players = models.IntegerField(default=1)
    holes_18_price = models.DecimalField(default=35.00, max_digits=10, decimal_places=2)
    num_9_players = models.IntegerField(default=1)
    holes_9_price = models.DecimalField(default=20.00, max_digits=10, decimal_places=2)
    num_18_carts = models.IntegerField(default=1)
    num_9_carts = models.IntegerField(default=1)
    cart_9_price = models.DecimalField(default=9.00, max_digits=10, decimal_places=2)
    cart_18_price = models.DecimalField(default=12.00, max_digits=10, decimal_places=2)
    golf_subtotal = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    golf_tax=models.DecimalField(default=.05, max_digits=10, decimal_places=2)
    golf_total=models.DecimalField(default=.05, max_digits=10, decimal_places=2)
    
    def save(self,*args,**kwargs):
        self.holes_18_price=float(self.num_18_players*self.holes_18_price)
        self.holes_9_price=float(self.holes_9_price*self.num_9_players)
        self.cart_9_price=float(self.cart_9_price*self.num_9_carts)
        self.cart_18_price=float(self.cart_18_price*self.num_18_carts)
        self.golf_subtotal=float(self.cart_18_price+self.cart_9_price+self.holes_18_price+self.holes_9_price)
        self.golf_tax=float(self.cart_18_price+self.cart_9_price+self.holes_18_price+self.holes_9_price)*.05
        self.golf_total=float(self.golf_subtotal+self.golf_tax)
        super().save(*args, **kwargs)


    def __str__(self):
      return self.gp_id


