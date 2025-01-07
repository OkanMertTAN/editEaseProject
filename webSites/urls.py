from django.urls import path
from . import views


urlpatterns = [
    path('hakkımızda/', views.webSitesAbout, name='webSitesAbout'),
]

urlpatterns = [
    path('anasayfa/', views.webSites, name='webSites'),
]

urlpatterns = [
    path('blog/', views.webSitesBlog, name='webSitesBlog'),
]

urlpatterns = [
    path('galeri/', views.webSitesGallery, name='webSitesGallery'),
]

urlpatterns = [
    path('hizmetler/', views.webSitesService, name='webSitesService'),
]


