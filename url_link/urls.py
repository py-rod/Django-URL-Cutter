from django.urls import path
from . import views


urlpatterns = [
    path('url/create', views.create_url_link, name='create_url'),
    path('url/all_url_links',
         views.all_url_links, name='all_url_links'),
    path('<slug:short_url>', views.redirect_urls, name='redirect_urls')
]
