from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import (
    ContactForm, 
    ServiceForm, 
    ReferenceForm, 
    AboutForm, 
    PersonnelForm, 
    HomepageContentForm, 
    GalleryForm,
    ContactFormSocialMedia,
    HomepageFotoForm
)

def cmsDashboard(request):
    return render(request, 'cmsHomePage.html')

def cmsStatus(request):
    return render(request, 'cmsStatus.html')

def cmsContentsUpdate(request):
    if request.method == 'POST':
        formType = request.POST.get('formType', '')

        if formType == 'contactForm':

            contactName=request.POST.get('contactName', '')
            contactAdress=request.POST.get('contactAdress', '')
            contactTel=request.POST.get('contactTel', '')
            contactFaks=request.POST.get('contactFaks', '')
            

            ContactForm.objects.create(contactName=contactName,contactAdress=contactAdress,contactTel=contactTel, contactFaks=contactFaks).save()

            
           
        elif formType == 'contactFormSocialMedia':

            contactİnst=request.POST.get('contactİnst', '')
            contactLinke=request.POST.get('contactLinke', '')
            contactFace=request.POST.get('contactFace', '')

            new_ContactFormSocialMedia = ContactFormSocialMedia.objects.create(contactİnst=contactİnst,contactLinke=contactLinke,contactFace=contactFace)
            new_ContactFormSocialMedia.save()

        elif formType == 'serviceForm':

            serviceName=request.POST.get('serviceName', '')
            serviceFoto=request.FILES.get('serviceFoto', '')
            serviceDesc=request.POST.get('serviceDesc', '')

            newServiceForm = ServiceForm.objects.create(serviceName=serviceName, serviceFoto=serviceFoto, serviceDesc=serviceDesc)

            newServiceForm.save()

        elif formType == 'referenceForm':

            referansName=request.POST.get('referansName', '')
            referansUrl=request.POST.get('referansUrl', '')
            
            new_ReferenceForm=ReferenceForm.objects.create(referansName=referansName, referansUrl=referansUrl)
            new_ReferenceForm.save()

        elif formType == 'aboutForm':

            aboutText=request.POST.get('aboutText', '')
            aboutFile=request.FILES.get('aboutFile', '')


            new_AboutForm = AboutForm.objects.create(aboutFile=aboutFile, aboutText=aboutText)
            new_AboutForm.save()

        elif formType == 'personnelForm':

            personelName=request.POST.get('personelName', '')
            personelDesc=request.POST.get('personelDesc', '')
            personelFoto=request.FILES.get('personelFoto', '')
            
            new_PersonnelForm = PersonnelForm.objects.create(personelName=personelName, personelDesc=personelDesc, personelFoto=personelFoto)
            new_PersonnelForm.save()

        elif formType == 'homepageContentForm':

            mainText=request.POST.get('mainText')
            mainDescText=request.POST.get('mainDescText')
            
            
            new_HomepageContentForm=HomepageContentForm.objects.create(mainText=mainText, mainDescText=mainDescText)

            new_HomepageContentForm.save()
        
        elif formType == 'homepageFotoForm':
            anaSayfaFoto=request.FILES.get('anaSayfaFoto','')

            new_HomepageFotoForm = HomepageFotoForm.objects.create(anaSayfaFoto=anaSayfaFoto)
            new_HomepageFotoForm.save()


        elif formType == 'otelForm':

            fotoName=request.POST.get('fotoName', '')
            statementWeb=request.POST.get('statementWeb', '')
            fotoFile=request.FILES.get('fotoFile', '')
            optionWeb=request.POST.get('optionWeb', '')

            new_GalleryForm=GalleryForm.objects.create(fotoName=fotoName, statementWeb=statementWeb, fotoFile=fotoFile, optionWeb=optionWeb)
            new_GalleryForm.save()

        return HttpResponseRedirect(reverse('cmsContentsUpdate'))

    return render(request, 'cmsContentsUpdate.html', {})
