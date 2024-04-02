from django.urls import path
from . import views


urlpatterns = [
    path('create_new_qr_codes', views.create_qr_codes,
         name='create_new_qr_codes'),
    path('all_qr_codes', views.all_qr_codes, name='all_qr_codes')
]
