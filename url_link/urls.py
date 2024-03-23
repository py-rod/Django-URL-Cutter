from django.urls import path
from . import views


urlpatterns = [
    path('create_new_url_short', views.create_url_link, name='create_url'),
    path('all_url_links',
         views.all_url_links, name='all_url_links'),
    path('<slug:short_url>', views.redirect_urls, name='redirect_urls')
]
