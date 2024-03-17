from django.urls import path
from . import views


urlpatterns = [
    path("menu_shortened", views.menu_shortened, name="menu_shortened"),
    path('create_new_url', views.create_url_link, name='create_url'),
]
