from django.shortcuts import render, redirect
from .models import Customer, Golf_purchases, Misc_purchases, Golf_Data
from .forms import CustomerForm, GolfPurchasesForm, Misc_purchasesForm, GolfDataForm
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_view(request):
    return render(request, 'golfproapp/home.html')

@login_required(redirect_field_name="{% url 'login' %}")
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

@login_required(redirect_field_name="{% url 'login' %}")
def customer_update_view(request, customer_id):
    customer = Customer.objects.get(customer_id=customer_id)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect ('customer_list')
    return render(request, 'golfproapp/customer_form.html', {'form': form})

@login_required(redirect_field_name="{% url 'login' %}")
def customer_delete_view(request, customer_id):
    customer = Customer.objects.get(customer_id=customer_id)
    if request.method == 'POST':
        customer.delete()
        return redirect ('customer_list')
    return render(request, 'golfproapp/cust_confirm_del.html', {'customer ID': customer_id})

@login_required(redirect_field_name="{% url 'login' %}")
def golf_purchase_create_view(request):
    form = GolfPurchasesForm()
    if request.method == 'POST':
        form = GolfPurchasesForm(request.POST)
        if form.is_valid():
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
    
@login_required(redirect_field_name="{% url 'login' %}")    
def golf_purchases_update_view(request, gp_id):
    golfpurchase = Golf_purchases.objects.get(gp_id=gp_id)
    form = GolfPurchasesForm(instance=golfpurchase)
    if request.method == 'POST':
        form = GolfPurchasesForm(request.POST, instance=golfpurchase)
        if form.is_valid():
            form.save()
            return redirect ('golf_purchase_list_view')
    return render(request, 'golfproapp/purchase_create.html', {'form': form})

@login_required(redirect_field_name="{% url 'login' %}")
def golf_purchases_delete_view(request, gp_id):
    gpurchase = Golf_purchases.objects.get(gp_id=gp_id)
    if request.method == 'POST':
        gpurchase.delete()
        return redirect ('golf_purchase_list_view')
    return render(request, 'golfproapp/purch_confirm_del.html', {'gp_id': gp_id})

def golf_purchase_success_view(request,gp_id):
    golfpurchase = Golf_purchases.objects.get(gp_id=gp_id)
    form = GolfPurchasesForm(request.GET, instance=golfpurchase)
    return render(request, 'golfproapp/gp_success.html', {'form': form})

@login_required(redirect_field_name="{% url 'login' %}")
def misc_purchase_create_view(request):
    form = Misc_purchasesForm()
    if request.method == 'POST':
        form = Misc_purchasesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('misc_purchase_list')
    return render(request, 'golfproapp/misc_purchase_create.html',{'form':form})

class misc_purchases_list_view(ListView): 
    model = Misc_purchases
    template_name = 'misc_purchase_list'
    context_object_name='misc_purchase_object_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
    
@login_required(redirect_field_name="{% url 'login' %}")
def misc_purchases_update_view(request, purch_id):
    miscpurchase = Misc_purchases.objects.get(purch_id=purch_id)
    form = Misc_purchasesForm(instance=miscpurchase)
    if request.method == 'POST':
        form = Misc_purchasesForm(request.POST, instance=miscpurchase)
        if form.is_valid():
            form.save()
            return redirect ('misc_purchase_list')
    return render(request, 'golfproapp/misc_purchase_create.html', {'form': form})

@login_required(redirect_field_name="{% url 'login' %}")
def misc_purchases_delete_view(request, purch_id):
    mpurchase = Misc_purchases.objects.get(purch_id=purch_id)
    if request.method == 'POST':
        mpurchase.delete()
        return redirect ('misc_purchase_list')
    return render(request, 'golfproapp/misc_confirm_del.html', {'purch_id': purch_id})

@login_required(redirect_field_name="{% url 'login' %}")
def create_teetime_view(request):
    form = GolfDataForm()
    if request.method == 'POST':
        form = GolfDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tee_time_list')
    return render(request, 'golfproapp/tee_time.html', {'form': form})

class tee_time_list_view(ListView): 
    model = Golf_Data
    template_name = 'golfproapp/tee_times_list.html'
    context_object_name='golf_data_object_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

@login_required(redirect_field_name="{% url 'login' %}")
def tee_time_update_view(request, tee_time_id):
    tbookupd = Golf_Data.objects.get(tee_time_id=tee_time_id)
    form = GolfDataForm(instance=tbookupd)
    if request.method == 'POST':
        form = GolfDataForm(request.POST, instance=tbookupd)
        if form.is_valid():
            form.save()
            return redirect ('tee_times_list')
    return render(request, 'golfproapp/tee_time.html', {'form': form})

@login_required(redirect_field_name="{% url 'login' %}")
def tee_time_delete_view(request, tee_time_id):
    dbookupd = Golf_Data.objects.get(tee_time_id=tee_time_id)
    if request.method == 'POST':
        dbookupd.delete()
        return redirect ('tee_time_list')
    return render(request, 'golfproapp/tee_time_del.html', {'tee_time_id': tee_time_id})
