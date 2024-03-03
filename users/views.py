from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import make_password


from .forms import UserCreationForm, AuthenticationForm
from .decorators import user_not_authenticated
# Create your views here.


@user_not_authenticated
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect("home")
        else:
            for error in list(form.errors.values()).pop():
                messages.error(request, error)
    else:
        form = UserCreationForm()

    return render(request, "signup.html", {
        "form": form
    })


@user_not_authenticated
def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logueado con exito")
                return redirect("home")
    else:
        form = AuthenticationForm()

    return render(request, "signin.html", {
        "form": form
    })


@login_required(login_url="signin")
def close_session(request):
    logout(request)
    return redirect("home")
