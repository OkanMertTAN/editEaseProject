from django.urls import path
from . import views

urlpatterns = [
    path('anasayfa/', views.webSites, name='webSites'),  # Anasayfa URL'si
    path('hakkımızda/', views.webSitesAbout, name='webSitesAbout'),  # Hakkımızda URL'si
    path('blog/', views.webSitesBlog, name='webSitesBlog'),
    path('galeri/', views.webSitesGallery, name='webSitesGallery'),
    path('hizmetler/', views.webSitesService, name='webSitesService'),
]
