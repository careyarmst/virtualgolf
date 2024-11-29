from django.urls import path
from . import views

urlpatterns = [
path('', views.home_view, name='home'),
path('create/', views.customer_create_view, name='customer_create'),
path('list/', views.customer_list_view, name='customer_list'),
path('update/<int:customer_id>/', views.customer_update_view, name='customer_update'),
path('delete/<int:customer_id>/', views.customer_delete_view, name='customer_delete'),
]