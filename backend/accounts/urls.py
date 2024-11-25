from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('signup/', include('dj_rest_auth.registration.urls')),
    path('<str:username>/', views.get_user_profile, name='get_my_page'),
    path('<str:username>/update/', views.update_profile, name='update_user'),
    path('<str:username>/journals/', views.user_journal_list, name='user_journal_list'),
]
