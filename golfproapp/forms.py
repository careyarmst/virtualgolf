from django import forms
from .models import Customer, Golf_purchases, Misc_purchases, Golf_Data
import calculation

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

class Misc_purchasesForm(forms.ModelForm):
    class Meta: 
        model = Misc_purchases
        fields = '__all__'
        labels = {
            'inv_id': 'Inventory ID',
            'inv_description' : 'Item Description',
            'misc_quantity' : 'Quantity',
            'misc_price' : 'Price',
            'misc_subtotal':'Subtotal',
            'misc_tax': 'Tax',
            'misc_total': 'Total'
        }
        widget = {
            'inv_id': forms.NumberInput(
                attrs={'placeholder':'e.g. 1', 'class':'form-control'}),
            'inv_description': forms.TextInput(
                attrs={'placeholder':'e.g. S12345', 'class':'form-control'}),
            'misc_quantity': forms.NumberInput(
                attrs={'placeholder':'e.g. 19.99', 'class':'form-control'}),
            'misc_price': forms.NumberInput(
                attrs={'placeholder':'e.g. 19.99', 'class':'form-control'}),
            'misc_subtotal': forms.NumberInput(
                attrs={'placeholder':'e.g. 19.99', 'class':'form-control'}),
            'misc_tax': forms.NumberInput(
                attrs={'placeholder':'e.g. 19.99', 'class':'form-control'}),
            'misc_total': forms.NumberInput(
                attrs={'placeholder':'e.g. 19.99', 'class':'form-control'}),
        }


class GolfDataForm(forms.ModelForm):
    class Meta:
        model = Golf_Data
        fields = '__all__'
        labels = {
            'customer_id': 'Golf Customer ID',
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

class GolfPurchasesForm(forms.ModelForm):
    customer_id = forms.ModelChoiceField(queryset=Customer.objects.all())
    class Meta:
        model = Golf_purchases
        fields = ['customer_id', 'gp_date', 'gp_id', 'holes_18_price', 'holes_9_price', 'cart_18_price', 'cart_9_price', 'golf_subtotal', 'golf_tax', 'golf_total']
        labels = {
            'gp_id': 'Golf Purchase ID',
            'gp_date': 'Golf Purchase Date',
            'holes_18_price' : 'Golf Price (18 Holes)',
            'holes_9_price' : 'Golf Price (9 Holes)',
            'cart_18_price': 'Cart Price (18 Holes)',
            'cart_9_price' : 'Cart Price (9 Holes)',
            'golf_subtotal': 'Golf Subtotal',
            'golf_tax': 'Golf Tax',
            'golf_total': 'Golf Total'

        }
        widgets = {
            'customer_id': forms.NumberInput(
                attrs={'placeholder':'e.g. 1', 'class':'form-control'}),
            'gp_id': forms.NumberInput(
                attrs={'placeholder':'e.g. Yes/No', 'class':'form-control'}),
            'gp_date': forms.DateInput(
                attrs={'placeholder':'e.g. Yes/No', 'class':'form-control'}),
            'holes_18_price': forms.NumberInput(
                attrs={'placeholder':'e.g. Bob', 'class':'form-control'}),
            'holes_9_price': forms.NumberInput(
                attrs={'placeholder':'e.g. Smith', 'class':'form-control'}),
            'cart_18_price': forms.NumberInput(
                attrs={'placeholder':'e.g. 201-331-2412', 'class':'form-control'}),
            'cart_9_price': forms.NumberInput(
                attrs={'placeholder':'e.g. bob@aol.com', 'class':'form-control'}),
            'golf_subtotal': forms.NumberInput(
                attrs={'placeholder':'e.g. bob@aol.com', 'class':'form-control'}),
            'golf_tax': forms.NumberInput(
                attrs={'placeholder':'e.g. bob@aol.com', 'class':'form-control'}),
            'golf_total': forms.NumberInput(
                attrs={'placeholder':'e.g. bob@aol.com', 'class':'form-control'}),
        }

