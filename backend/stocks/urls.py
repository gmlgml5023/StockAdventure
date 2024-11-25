# stocks/urls.py
from django.urls import path
from . import views

app_name = 'stocks'

urlpatterns = [
    path('', views.stock_list, name='stock-list'),
    path('update/', views.stock_update, name='stock-update'),
    path('<str:stock_id>/like/', views.stock_like, name='stock-like'),  # 좋아요 토글 엔드포인트

]