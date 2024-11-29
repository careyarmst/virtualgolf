from django import forms
from .models import *

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        labels = {
            'customer_id': 'Customer ID',
            'is_golfer': 'Golfer Yes or No',
            'fname' : 'First Name',
            'lname' : 'Last Name',
            'g_phone': 'Phone Number',
            'g_email': 'Email'
        }
        widgets = {
            'customer_id': forms.NumberInput(
                attrs={'placeholder':'e.g. 1', 'class':'form-control'}),
            'is_golfer': forms.TextInput(
                attrs={'placeholder':'e.g. Yes/No', 'class':'form-control'}),
            'fname': forms.TextInput(
                attrs={'placeholder':'e.g. Bob', 'class':'form-control'}),
            'lname': forms.TextInput(
                attrs={'placeholder':'e.g. Smith', 'class':'form-control'}),
            'g_phone': forms.TextInput(
                attrs={'placeholder':'e.g. 201-331-2412', 'class':'form-control'}),
            'g_email': forms.TextInput(
                attrs={'placeholder':'e.g. bob@aol.com', 'class':'form-control'}),
        }

class InvOptionsForm(forms.ModelForm):
    class Meta:
        model = inv_options
        fields = '__all__'
        labels = {
            'opt_name': 'Category'
        }
        widget = {
            'opt_name': forms.TextInput(
                attrs={'placeholder':'e.g. shirt', 'class':'form-control'}),
        }
        

class InventoryForm(forms.ModelForm):
    class Meta:
        model = inventory
        fields = '__all__'
        labels = {
            'inv_id': 'Inventory ID',
            'inv_options': 'Category',
            'inv_description' : 'Item Description',
            'price' : 'Item price'
        }
        widget = {
            'inv_id': forms.NumberInput(
                attrs={'placeholder':'e.g. 1', 'class':'form-control'}),
            'inv_options': forms.TextInput(
                attrs={'placeholder':'e.g. shirt', 'class':'form-control'}),
            'inv_description': forms.TextInput(
                attrs={'placeholder':'e.g. S12345', 'class':'form-control'}),
            'price': forms.NumberInput(
                attrs={'placeholder':'e.g. 19.99', 'class':'form-control'}),

        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = order
        fields = '__all__'
        labels = {
            'products': 'Products in Order',
            'created_at': 'Order Date'
        }
        widget = {
            'products': forms.TextInput(
                attrs={'placeholder':'e.g. shirt', 'class':'form-control'}),
            'created_at': forms.TextInput(
                attrs={'placeholder':'e.g. S12345', 'class':'form-control'}),
        }


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'
        labels = {
            'order': 'Products in Order',
            'inventory': 'Inventory Data',
            'quantity': 'Quantity'
        } 
        widget = {
            'order': forms.TextInput(
                attrs={'placeholder':'e.g. S12345', 'class':'form-control'}),
            'inventory': forms.NumberInput(
                attrs={'placeholder':'e.g. 19.99', 'class':'form-control'}),
            'quantity': forms.NumberInput(
                attrs={'placeholder':'e.g. 10', 'class':'form-control'}),
        }

class GolfingForm(forms.ModelForm):
    class Meta:
        model = Golfing
        fields = '__all__'
        labels = {
            'customer_id': 'Customer ID',
            'tee_time': 'Tee Time',
            'no_in_party': 'Number in Group',
            'avg_grp_hcp': 'Group Average Handicap'
        } 
        widget = {
             'customer_id': forms.NumberInput(
                attrs={'placeholder':'e.g. 1', 'class':'form-control'}),
            'tee_time': forms.TextInput(
                attrs={'placeholder':'e.g. shirt', 'class':'form-control'}),
            'no_in_party': forms.NumberInput(
                attrs={'placeholder':'e.g. S12345', 'class':'form-control'}),
            'avg_grp_hcp': forms.NumberInput(
                attrs={'placeholder':'e.g. 19.99', 'class':'form-control'}),
        }
class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'
        labels = {
            'subtotal': 'Subtotal',
            'tax': 'Tax',
            'total': 'Total'
        } 
        widget = {
          'subtotal': forms.NumberInput(
                attrs={'placeholder':'e.g. 1', 'class':'form-control'}),
            'tax': forms.TextInput(
                attrs={'placeholder':'e.g. shirt', 'class':'form-control'}),
            'total': forms.NumberInput(
                attrs={'placeholder':'e.g. S12345', 'class':'form-control'}),
  
        }
