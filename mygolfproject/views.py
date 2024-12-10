from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm


def register_user(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            success_url = reverse("home")
            return HttpResponseRedirect(success_url)
    else:
        form = UserCreationForm()

    context = {"form": form}

    return render(request, "registration/registration_form.html", context)
