from django.urls import path
from . import views

urlpatterns = [
    path('Ana_Sayfa_Dashboard/', views.cmsDashboard, name='cmsDashboard'),
    path('Icerik_Yönetim_Dashboard/', views.cmsContentsUpdate, name='cmsContentsUpdate'),
    path('Icerik_Dashboard/', views.cmsStatus, name='cmsStatus'),
]
