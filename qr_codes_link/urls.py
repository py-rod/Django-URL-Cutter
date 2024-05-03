from django.urls import path
from . import views


urlpatterns = [
    path('qr_codes/create', views.create_qr_codes,
         name='create_new_qr_codes'),
    path('qr_codes/all_qr_codes/', views.all_qr_codes, name='all_qr_codes'),
    path('<slug:short_url>/', views.redirect_qr_codes, name='redirect_qr'),
    path('qr/delete/<int:id>', views.delete_qr, name='delete_qr')
]
