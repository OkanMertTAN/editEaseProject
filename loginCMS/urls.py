from django.urls import path
from . import views

urlpatterns = [
    path('loginCMS/', views.loginCMS, name='loginCMS'),  # Login sayfası
    path('logoutCMS/', views.logoutCMS, name='logoutCMS'),  # Oturum kapatma (dashboard'dan gelir)
]
