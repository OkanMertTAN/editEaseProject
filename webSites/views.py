from django.shortcuts import render
from django.http import HttpResponse
from cmsDashboard.models import(
    HomepageContentForm,
    HomepageFotoForm
)

def webSites(request):

    return render(request, 'index.html')
    #return HttpResponse("Merhaba!")

def webSitesAbout(request):
    return render(request, 'about.html')
    #return HttpResponse("Merhaba!")

def webSitesGallery(request):
    return render(request, 'gallery.html')

def webSitesBlog(request):
    return render(request, 'blog.html')

def webSitesService(request):
    return render(request, 'service.html')



