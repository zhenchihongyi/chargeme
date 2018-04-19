from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views


app_name = 'accounts'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout$', auth_views.logout, name='logout'),
    url(r'^new$', views.new, name='new'),
    url(r'^create$', views.create, name='create'),
    url(r'^order_list$', views.order_list, name='order_list'),
]