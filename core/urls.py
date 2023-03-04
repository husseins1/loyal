from django.urls import path
from . import views


urlpatterns = [
     path('send/<phone_number>/', views.send,name='send'),
    path('print id/<id>/', views.print_id, name='print id'),
    path('analytics', views.analytics, name='analytics'),
    path('orders', views.getOrders, name='orders'),
]

