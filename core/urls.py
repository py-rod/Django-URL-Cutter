"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("index.urls")),
    path('accounts/', include("users.urls")),
    path('dashboard/', include("dashboard.urls")),
    path('', include("url_link.urls")),
    path('', include("qr_codes_link.urls")),
    path('analytics/', include('analytics.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('qr_code.urls', namespace='qr_code')),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

SERVE_QR_CODE_IMAGE_PATH = 'qr-code-image/'
