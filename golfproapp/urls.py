from django.urls import path
from . import views
from .models import Golf_purchases

urlpatterns = [
path('', views.home_view, name='home'),
path('create/', views.customer_create_view, name='customer_create'),
path('list/', views.customer_list_view, name='customer_list'),
path('update/<int:customer_id>/', views.customer_update_view, name='customer_update'),
path('delete/<int:customer_id>/', views.customer_delete_view, name='customer_delete'),
path('gpcreate/', views.golf_purchase_create_view, name='golf_purchase_create'),
path('gplist/', views.golf_purchases_list_view.as_view(), name = 'golf_purchase_list_view'),
path('gpupdate/<int:gp_id>/', views.golf_purchases_update_view, name='golf_purchase_update'),
path('gpdelete/<int:gp_id>/', views.golf_purchases_delete_view, name='golf_purchase_delete'),
path('gpsuccess/<int:gp_id>/', views.golf_purchase_success_view, name='gp_success'),
path('mpcreate/', views.misc_purchase_create_view, name='misc_purchase_create'),
path('mplist/', views.misc_purchases_list_view.as_view(), name = 'misc_purchase_list'),
path('mpupdate/<int:purch_id>/', views.misc_purchases_update_view, name='misc_purchase_update'),
path('mpdelete/<int:purch_id>/', views.misc_purchases_delete_view, name='misc_purchase_delete'),
path('create_teetime/', views.create_teetime_view, name='create_teetime'),
path('teetimes/',views.tee_time_list_view.as_view(), name = 'tee_time_list'),
path('teeupdate/<int:tee_time_id>/', views.tee_time_update_view, name='tee_time_update'),
path('teedelete/<int:tee_time_id>/', views.tee_time_delete_view, name='tee_time_delete'),

]