from django.db import models

# Create your models here.

class LoginCMSInfo(models.Model):

    username = models.CharField(max_length=150, null=False)
    password = models.CharField(max_length=150, null=False)

    def __str__(self):
        return "LoginCMS"