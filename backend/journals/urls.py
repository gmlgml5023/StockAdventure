from django.urls import path
from . import views

app_name = 'journals'
urlpatterns = [
    # 매매일지 목록
    path('', views.journal_list),
    # 매매일지 상세
    path('<int:journal_pk>/', views.journal_detail),
]