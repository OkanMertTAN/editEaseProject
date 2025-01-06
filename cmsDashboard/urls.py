from django.urls import path
from . import views

urlpatterns = [
    path('cmsDashboard/', views.cmsDashboard, name='cmsDashboard'),
]
