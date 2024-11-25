from django.urls import path
from . import views

app_name = 'investment_style'
urlpatterns = [
    path('test/', views.calculate_investment_style, name='investment_test'),
    path('result/', views.investment_test_result, name='investment_result'),
]