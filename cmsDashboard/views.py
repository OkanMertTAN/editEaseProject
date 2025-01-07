from django.shortcuts import render
from django.http import HttpResponse

def cmsDashboard(request):
    #return HttpResponse("Hello world!")
    return render(request, 'cmsHomePage.html')

def cmsContentsUpdate(request):
    return render(request, 'cmsContentsUpdate.html')