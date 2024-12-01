from django.shortcuts import render, redirect
from .models import Customer, Golf_purchases
from .forms import CustomerForm, GolfPurchasesForm
from django.http import HttpResponse
# Create your views here.

def home_view(request):
    return render(request, 'golfproapp/home.html')

def customer_create_view(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('customer_list')
    return render(request, 'golfproapp/customer_form.html', {'form': form})

def customer_list_view(request):
    customers = Customer.objects.all()
    return render(request,'golfproapp/customer_list.html', {'customers': customers})

def customer_update_view(request, customer_id):
    customer = Customer.objects.get(customer_id=customer_id)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect ('customer_list')
    return render(request, 'golfproapp/customer_form.html', {'form': form})

def customer_delete_view(request, customer_id):
    customer = customer.objects.get(customer_id=customer_id)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'golfproapp/cust_confirm_del.html', {'customer' : customer})

def golf_purchases_create_view(request):
    form = GolfPurchasesForm()
    if request.method == 'POST':
        form = GolfPurchasesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
    return render(request, 'golfproapp/golf_purchases_form.html', {'form': form})

#def golf_purchases_list_view(request,golf_purchase_id = "*"):
 #   golf_purchase_id = Golf_purchases.objects.get(golf_purchase_id=golf_purchase_id)
  #  Golf_purchases = Golf_purchases.objects.all()
   # return render(request,'golfproapp/customer_list.html', {'Golf_purchases': Golf_purchases})


def golf_purchases_update_view(request, golf_purchase_id):
    golf_purchase_id = Golf_purchases.objects.get(golf_purchase_id=golf_purchase_id)
    form = GolfPurchasesForm(instance=golf_purchase_id)
    if request.method == 'POST':
        form = GolfPurchasesForm(request.POST, instance=golf_purchase_id)
        if form.is_valid():
            form.save()
            return redirect ('home')
    return render(request, 'golfproapp/golf_purchases_form.html', {'form': form})

def golf_purchases_delete_view(request, golf_purchase_id):
    golf_purchase_id = Golf_purchases.objects.get(golf_purchase_id=golf_purchase_id)
    if request.method == 'POST':
        golf_purchase_id.delete()
        return redirect('home')
    return render(request, 'golfproapp/purch_confirm_del.html', {'Golf_purchase' : golf_purchase_id})

