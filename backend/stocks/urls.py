# stocks/urls.py
from django.urls import path
from . import views

app_name = 'stocks'

urlpatterns = [
    path('', views.stock_list, name='stock-list'),
    path('update/', views.stock_update, name='stock-update'),
]