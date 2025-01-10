from django.db import models

# Create your models here.

class database_form_db(models.Model):
    formType = models.CharField(max_length=100, null=False, blank=False) 

    fotoName = models.CharField(max_length=100, null=True, blank=False, default='DefaultValue')
    statementWeb = models.TextField(null=True, default='DefaultValue')
    fotoFile = models.ImageField(upload_to='images', null=True)
    optionWeb = models.CharField(max_length=100, null=True, blank=False, default='DefaultValue')

    mainText = models.CharField(max_length=200, null=True, blank=False, default='DefaultValue')
    mainDescText = models.TextField(null=True, default='DefaultValue')

    anaSayfaFoto = models.ImageField(upload_to='images', null=True)

    personelName = models.CharField(max_length=20, null=False, blank=False) 
    personelDesc = models.TextField(null=True, default='DefaultValue')
    personelFoto = models.ImageField(upload_to='images', null=True)

    aboutText = models.TextField(null=True, default='DefaultValue')
    aboutFile = models.ImageField(upload_to='images', null=True)

    referansName = models.CharField(max_length=100, null=True, blank=False, default='DefaultValue')
    referansUrl = models.CharField(max_length=150, null=True, blank=False, default='DefaultValue')

    serviceName = models.CharField(max_length=100, null=True, blank=False, default='DefaultValue')
    serviceFoto = models.ImageField(upload_to='images', null=True)
    serviceDesc = models.TextField(null=True, default='DefaultValue')

    contactName = models.CharField(max_length=100, null=True, blank=False, default='DefaultValue')
    contactAdress = models.TextField(null=True, default='DefaultValue')
    contactTel = models.CharField(max_length=150, null=True, blank=False, default='DefaultValue')
    contactFaks = models.CharField(max_length=150, null=True, blank=False, default='DefaultValue')

    contactİnst = models.CharField(max_length=150, null=True, blank=False, default='DefaultValue')
    contactLinke = models.CharField(max_length=150, null=True, blank=False, default='DefaultValue')
    contactFace = models.CharField(max_length=150, null=True, blank=False, default='DefaultValue')

    def __str__(self):
        return self.formType

