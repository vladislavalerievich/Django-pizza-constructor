from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('order/<int:order_id>/', views.order, name='order'),
    path('message/', views.message, name='message'),
]
