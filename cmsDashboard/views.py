from django.shortcuts import render
from django.http import HttpResponse
from .models import Common_database

def cmsDashboard(request):
    #return HttpResponse("Hello world!")
    return render(request, 'cmsHomePage.html')

def cmsContentsUpdate(request):

    if request.method == 'POST':
        mainText = request.POST['mainText']
        mainDescText = request.POST['mainDescText']

        new_Common_database = Common_database(mainText=mainText, mainDescText=mainDescText)
        new_Common_database.save()

    return render(request, 'cmsContentsUpdate.html' ,{})




