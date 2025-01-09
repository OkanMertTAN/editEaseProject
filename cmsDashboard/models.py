from django.db import models

# Create your models here.

class Common_database(models.Model):
    mainText = models.CharField(max_length=200, null=False, blank=False)
    mainDescText = models.TextField()


    def __str__(self):
        return self.mainText
    
    #Bu veritabanı silincektir. 