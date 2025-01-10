from .models import database_form_db
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render


def cmsDashboard(request):
    #return HttpResponse("Hello world!")
    return render(request, 'cmsHomePage.html')

def cmsContentsUpdate(request):
    
    if request.method == 'POST': 
        formType = request.POST.get('formType','')

        fotoName = request.POST.get('fotoName','')
        statementWeb = request.POST.get('statementWeb','')
        fotoFile = request.FILES.get('fotoFile')
        optionWeb = request.POST.get('optionWeb','')

        mainText = request.POST.get('mainText','')
        mainDescText = request.POST.get('mainDescText','')

        anaSayfaFoto = request.FILES.get('anaSayfaFoto','')

        personelName = request.POST.get('personelName','')
        personelDesc = request.POST.get('personelDesc','')
        personelFoto = request.FILES.get('personelFoto')

        aboutText = request.POST.get('aboutText','')
        aboutFile = request.POST.get('aboutFile','')

        referansName = request.POST.get('referansName','')
        referansUrl = request.POST.get('referansUrl','')

        serviceName = request.POST.get('serviceName','')
        serviceFoto = request.FILES.get('serviceFoto')
        serviceDesc = request.POST.get('serviceDesc','')

        contactName = request.POST.get('contactName','')
        contactAdress = request.POST.get('contactAdress','')
        contactTel = request.POST.get('contactTel','')
        contactFaks = request.POST.get('contactFaks','')

        contactİnst = request.POST.get('contactİnst','')
        contactLinke = request.POST.get('contactLinke','')
        contactFace = request.POST.get('contactFace','')

        new_form = database_form_db(formType=formType, fotoName=fotoName, statementWeb=statementWeb, fotoFile=fotoFile, optionWeb=optionWeb, mainText=mainText, mainDescText=mainDescText, anaSayfaFoto=anaSayfaFoto, personelName=personelName, personelDesc=personelDesc, personelFoto=personelFoto, aboutText=aboutText, aboutFile=aboutFile, referansName=referansName, referansUrl=referansUrl, serviceName=serviceName, serviceFoto=serviceFoto, serviceDesc=serviceDesc, contactName=contactName, contactAdress=contactAdress, contactTel=contactTel, contactFaks=contactFaks, contactİnst=contactİnst, contactLinke=contactLinke, contactFace=contactFace)

        new_form.save()

        return HttpResponseRedirect(reverse('cmsContentsUpdate'))

    
    return render(request, 'cmsContentsUpdate.html', {})




