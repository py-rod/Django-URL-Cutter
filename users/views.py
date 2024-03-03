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
            messages.success(
                request, "Your account has been successfully created")
            return redirect("signin")
        else:
            for error in list(form.errors.values()).pop():
                messages.error(request, error)
    else:
        form = UserCreationForm()

    return render(request, "signup.html", {
        "form": form
    })


def redirect_signin_with_google(request):
    messages.error(
        request, "Something wrong here, it may be that you already have account!")
    return redirect("signin")


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
                messages.success(
                    request, f"Welcome {request.user.first_name} {request.user.last_name}")
                return redirect("home")
        else:
            for error in list(form.errors.values()).pop():
                messages.error(request, error)
    else:
        form = AuthenticationForm()

    return render(request, "signin.html", {
        "form": form
    })


@login_required(login_url="signin")
def close_session(request):
    logout(request)
    messages.info(request, "You have logged out.")
    return redirect("home")
