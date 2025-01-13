from django.urls import path
from . import views
from webSites.views import webSites

urlpatterns = [
    path('loginCMS/', views.loginCMS, name='loginCMS'),  # Login sayfası
    path('logoutCMS/', views.logoutCMS, name='logoutCMS'),  # Oturum kapatma (dashboard'dan gelir)
    path('anasayfa/', webSites, name='webSites')
]
