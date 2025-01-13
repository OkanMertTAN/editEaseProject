from django.shortcuts import render, redirect
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
def user_authenticated(request):
    return 'user_authenticated' in request.session



def logoutCMS(request):
    # Oturum bilgisini temizle
    request.session.flush()  # Oturum verilerini temizler
    return redirect('loginCMS')  # Login sayfasına yönlendir





def cmsDashboard(request):
    if not user_authenticated(request):
        return redirect('logoutCMS')  # Kullanıcı oturum açmamışsa login sayfasına yönlendir

    
    return render(request, 'cmsHomePage.html')

def cmsStatus(request):
    if not user_authenticated(request):
        return redirect('logoutCMS')  # Kullanıcı oturum açmamışsa login sayfasına yönlendir

   
    return render(request, 'cmsStatus.html')

def cmsContentsUpdate(request):
    if not user_authenticated(request):
        return redirect('logoutCMS')  # Kullanıcı oturum açmamışsa login sayfasına yönlendir


    
    
    if request.method == 'POST':
        formType = request.POST.get('formType', '')

        if formType == 'contactForm':

            contactName=request.POST.get('contactName', '')
            contactAdress=request.POST.get('contactAdress', '')
            contactTel=request.POST.get('contactTel', '')
            contactFaks=request.POST.get('contactFaks', '')
            

            new_ContactForm = ContactForm.objects.create(contactName=contactName,contactAdress=contactAdress,contactTel=contactTel, contactFaks=contactFaks)
            new_ContactForm.save()
            

        elif formType == 'contactFormSocialMedia':

            contactİnst=request.POST.get('contactİnst', '')
            contactLinke=request.POST.get('contactLinke', '')
            contactFace=request.POST.get('contactFace', '')

            ContactFormSocialMedia.objects.filter(id=12).update(contactİnst=contactİnst, contactLinke=contactLinke, contactFace=contactFace)
            

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


            AboutForm.objects.filter(id=9).update(aboutFile=aboutFile, aboutText=aboutText)

        elif formType == 'personnelForm':

            personelName=request.POST.get('personelName', '')
            personelDesc=request.POST.get('personelDesc', '')
            personelFoto=request.FILES.get('personelFoto', '')
            
            new_PersonnelForm = PersonnelForm.objects.create(personelName=personelName, personelDesc=personelDesc, personelFoto=personelFoto)
            new_PersonnelForm.save()

        elif formType == 'homepageContentForm':

            mainText=request.POST.get('mainText')
            mainDescText=request.POST.get('mainDescText')
            
            
            HomepageContentForm.objects.filter(id=4).update(mainText=mainText, mainDescText=mainDescText)

        
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
