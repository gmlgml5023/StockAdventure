# stocks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.stock_list, name='stock-list'),
    path('update/', views.stock_update, name='stock-update'),
]