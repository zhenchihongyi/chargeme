from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views


app_name = 'accounts'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login', views.login, {'template_name': 'accounts/login.html'}, name='login'),
#    url(r'^login/?station_id=(?P<battery_station_id>\d+)', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout$', auth_views.logout, name='logout'),
    url(r'^new$', views.new, name='new'),
    url(r'^create$', views.create, name='create'),
    url(r'^order_list', views.order_list, name='order_list'),
    url(r'^create_order$', views.create_order, name='create_order'),
    url(r'^return_to_indexpage', views.return_to_indexpage, name='return_to_indexpage'),

]