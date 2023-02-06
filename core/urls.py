from django.urls import path
from . import views


urlpatterns = [
     path('send/<phone_number>/', views.send,name='send'),
    
]

