from django.db import models


# contactFormSocialMedia 

class ContactFormSocialMedia(models.Model):
    contactİnst = models.CharField(max_length=500, null=True, blank=False)
    contactLinke = models.CharField(max_length=500, null=True, blank=False)
    contactFace = models.CharField(max_length=500, null=True, blank=False)

    def __str__(self):
        return "Social Media"
    
# Contact Form Model
class ContactForm(models.Model):
    contactName = models.CharField(max_length=100, null=True, blank=False, default='DefaultValue')
    contactAdress = models.TextField(null=True, default='DefaultValue')
    contactTel = models.CharField(max_length=150, null=True, blank=False, default='DefaultValue')
    contactFaks = models.CharField(max_length=150, null=True, blank=False, default='DefaultValue')
    

    def __str__(self):
        return "contactName"

# Service Form Model
class ServiceForm(models.Model):
    serviceName = models.CharField(max_length=100, null=True, blank=False, default='DefaultValue')
    serviceFoto = models.ImageField(upload_to='images/', null=True)
    serviceDesc = models.TextField(null=True, default='DefaultValue')

    def __str__(self):
        return self.serviceName

# Reference Form Model
class ReferenceForm(models.Model):
    referansName = models.CharField(max_length=100, null=True, blank=False, default='DefaultValue')
    referansUrl = models.CharField(max_length=150, null=True, blank=False, default='DefaultValue')

    def __str__(self):
        return self.referansName

# About Form Model
class AboutForm(models.Model):
    aboutText = models.TextField(null=True, default='DefaultValue')
    aboutFile = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return "About Form"

# Personnel Form Model
class PersonnelForm(models.Model):
    personelName = models.CharField(max_length=20, null=False, blank=False)
    personelDesc = models.TextField(null=True, default='DefaultValue')
    personelFoto = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.personelName

# Homepage Content Form Model
class HomepageContentForm(models.Model):
    mainText = models.CharField(max_length=200, null=True, blank=False, default='DefaultValue')
    mainDescText = models.TextField(null=True, default='DefaultValue')
    

    def __str__(self):
        return "Main Text"
    
class HomepageFotoForm(models.Model):
    anaSayfaFoto = models.ImageField(upload_to='images/', null=True)
    
    def __str__(self):
        return self.anaSayfaFoto.name

# Gallery Form Model
class GalleryForm(models.Model):
    fotoName = models.CharField(max_length=100, null=True, blank=False, default='DefaultValue')
    statementWeb = models.TextField(null=True, default='DefaultValue')
    fotoFile = models.ImageField(upload_to='images/', null=True)
    optionWeb = models.CharField(max_length=100, null=True, blank=False, default='DefaultValue')

    def __str__(self):
        return self.fotoName
