from django.urls import path
from . import views


urlpatterns = [
    path('create_qr_codes', views.create_qr_codes, name='create_qr_codes'),
]
