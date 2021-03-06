from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from users.forms import UserForm

# Create your views here.
def login_user(request):
    template = "registration/login.html"
    form = UserForm()
    context = {
        "form": form
    }
    return render(request, template, context)


def _logout(request):
    user = request.user 
    logout(request)
    return redirect("login_user")


def sign_in(request):
    if request.method == "POST":
        form = UserForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

            else:
                messages.success(request, "Invalid User Credentials")
                return redirect("login_user")

            return redirect("home")
