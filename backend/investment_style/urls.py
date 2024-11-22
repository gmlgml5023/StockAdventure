from django.urls import path
from . import views

app_name = 'investment_style'
urlpatterns = [
    path('test/', views.investment_test, name='investment_test'),
    path('result/', views.investment_result, name='investment_result'),
]