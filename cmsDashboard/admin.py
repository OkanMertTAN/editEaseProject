from django.contrib import admin
from .models import (
    ContactForm, ServiceForm, ReferenceForm, AboutForm,
    PersonnelForm, HomepageContentForm, GalleryForm, ContactFormSocialMedia, HomepageFotoForm
)

from loginCMS.models import(
    LoginCMSInfo
)

admin.site.register(ContactForm)
admin.site.register(ServiceForm)
admin.site.register(ReferenceForm)
admin.site.register(AboutForm)
admin.site.register(PersonnelForm)
admin.site.register(HomepageContentForm)
admin.site.register(GalleryForm)
admin.site.register(ContactFormSocialMedia)
admin.site.register(HomepageFotoForm)
admin.site.register(LoginCMSInfo)