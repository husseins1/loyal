from django.urls import path
from . import views


urlpatterns = [
     path('history/<id>/', views.history,name='history'),
    path('print id/<id>/', views.print_id, name='print id'),
    path('analytics', views.analytics, name='analytics'),
    path('orders', views.getOrders, name='orders'),
]

