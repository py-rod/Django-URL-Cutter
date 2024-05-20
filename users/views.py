from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.forms import PasswordResetForm


from .forms import UserCreationForm, AuthenticationForm, SetPasswordForm, Updateprofile
from .decorators import user_not_authenticated
from .token import account_activation_token

from url_link.models import ModelUrl
from qr_codes_link.models import ModelQR
from analytics.models import QRAnalytics, UrlAnalytics
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


def redirect_signin_whith_google_cancel(request):
    return redirect('signin')


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


@user_not_authenticated
def forgot_password(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            user_associated = get_user_model().objects.filter(Q(email=email)).first()
            if user_associated:
                subject = "Password Reset request"
                message = render_to_string("email_forgot_password.html", {
                    "user": user_associated,
                    "domain": get_current_site(request).domain,
                    "uid": urlsafe_base64_encode(force_bytes(user_associated.id)),
                    "token": account_activation_token.make_token(user_associated),
                    "protocol": "https" if request.is_secure() else "http"
                })
                email = EmailMessage(subject, message, to=[
                                     user_associated.email])
                email.content_subtype = "html"
                if email.send():
                    messages.success(
                        request, "Check your email for reset password")
                    return redirect("home")
    else:
        form = PasswordResetForm()
    return render(request, "forgot_password_reset_form.html", {
        "type": "send-email",
        "form": form
    })


@user_not_authenticated
def reset_password_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_user_model().objects.get(id=uid)
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        request.session["uid"] = uid
        messages.success(request, "Enter the new password")
        return redirect("reset_password_confirm")
    else:
        messages.error(request, "The link has been expired")
        return redirect("signin")


@user_not_authenticated
def reset_password_confirm(request):
    if request.method == "POST":
        uid = request.session.get("uid")
        user = get_user_model().objects.get(id=uid)
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your password has been set, enter the new password for sign in")
            return redirect("signin")
        else:
            for error in list(form.errors.values()).pop():
                messages.error(request, error)
    else:
        uid = request.session.get("uid")
        user = get_user_model().objects.get(id=uid)
        form = SetPasswordForm(user)
    return render(request, "forgot_password_reset_form.html", {
        "type": "new-password",
        "form": form
    })


@login_required(login_url='signin')
def settings_view(request):
    user = request.user

    form_display_name = Updateprofile(instance=user)
    form_change_password = SetPasswordForm(user)
    if request.method == 'POST':
        if 'display_name_form' in request.POST:
            form_display_name = Updateprofile(request.POST, instance=user)
            if form_display_name.is_valid():
                form_display_name.save()
                messages.success(request, 'Your display name has been change')
                return redirect('settings_view')
            else:
                for error in list(form_display_name.errors.values()).pop():
                    messages.error(request, error)

        elif 'change_password_form' in request.POST:
            form_change_password = SetPasswordForm(user, request.POST)
            if form_change_password.is_valid():
                form_change_password.save()
                messages.success(
                    request, 'Your password has been change. Now signin again')
                return redirect('settings_view')
            else:
                for error in list(form_change_password.errors.values()).pop():
                    messages.error(request, error)

    return render(request, 'settings_account.html', {
        'form_display_name': form_display_name,
        'form_change_password': form_change_password

    })


def delete_account(request):
    user = get_user_model().objects.get(email=request.user.email)

    model_url = ModelUrl.objects.filter(user=user).all()
    analytic_url = UrlAnalytics.objects.filter(creator=user).all()
    model_qr = ModelQR.objects.filter(user=user).all()
    analytic_qr = QRAnalytics.objects.filter(creator=user).all()
    analytic_url.delete()
    analytic_qr.delete()
    model_url.delete()
    model_qr.delete()

    user.delete()

    logout(request)
    messages.success(request, 'Your account has been delete')
    return redirect('home')
