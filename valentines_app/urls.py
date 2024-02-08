from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('send-card/', views.send_card, name='send_card'),
]
