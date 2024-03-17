from django.urls import path
from . import views


urlpatterns = [
    path('create_new_url_short', views.create_url_link, name='create_url'),
]
