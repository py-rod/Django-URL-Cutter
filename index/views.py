from django.shortcuts import render, redirect
from users.decorators import user_not_authenticated

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return render(request, "menu_urls.html")
    else:
        return render(request, "index.html")
