from django.shortcuts import render, redirect
from .models import Customer, Golf_purchases
from .forms import CustomerForm, GolfPurchasesForm
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
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

def golf_purchase_create_view(request):
    form = GolfPurchasesForm()
    if request.method == 'POST':
        form = GolfPurchasesForm(request.POST)
        if form.is_valid():
            get_holes_18_price = form.cleaned_data['holes_18_price']
            get_holes_9_price = form.cleaned_data['holes_9_price']
            get_cart_18_price = form.cleaned_data['cart_18_price']
            get_cart_9_price = form.cleaned_data['holes_18_price']
            subtotal = float(get_holes_18_price)+float(get_holes_9_price)+float(get_cart_18_price)+float(get_cart_9_price)
            tax = float(subtotal) * float(.05)
            total = float(subtotal) + float(tax)
            context = {
                'subtotal' :subtotal,
                'tax':tax,
                'total': total
            }
            form.save()
            return redirect ('golf_purchase_list_view')
    return render(request, 'golfproapp/purchase_create.html',{'form':form})

class golf_purchases_list_view(ListView): 
    model = Golf_purchases
    template_name = 'golf_purchases_list.html'
    context_object_name='golf_purchase_object_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
    
def golf_purchases_update_view(request, gp_id):
    golfpurchase = Golf_purchases.objects.get(gp_id=gp_id)
    form = GolfPurchasesForm(instance=golfpurchase)
    if request.method == 'POST':
        form = GolfPurchasesForm(request.POST, instance=golfpurchase)
        if form.is_valid():
            form.save()
            return redirect ('golf_purchase_list_view')
    return render(request, 'golfproapp/purchase_create.html', {'form': form})

def golf_purchases_delete_view(request, gp_id):
    golfpurchase = Golf_purchases.objects.get(gp_id=gp_id)
    if request.method == 'POST':
        gp_id.delete()
        return redirect('golfapp/golf_purchase_list.html')
    return render(request, 'golfproapp/purch_confirm_del.html', {'Golf_purchase' : golfpurchase})

def golf_purchase_success_view(request,gp_id):
    golfpurchase = Golf_purchases.objects.get(gp_id=gp_id)
    return render(request, 'golfproapp/gp_success.html', {'Golf_purchase' : golfpurchase})


