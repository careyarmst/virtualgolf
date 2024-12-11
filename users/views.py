from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            messages.success(request,("Oops that didn't work, try again"))
            return redirect('login')
    
    else:
        return render(request,'registration/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request,("You were logged out"))
    return redirect('home')

def register_user(request):
    if request.method == "POST":
         form = UserCreationForm(request.POST)
         if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request,("Registration Successful"))
            return redirect('home')
    else:
         form = UserCreationForm()          
    return render(request, 'registration/register_user.html', {'form':form,})

