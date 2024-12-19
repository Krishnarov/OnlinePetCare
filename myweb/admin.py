
from django.contrib import admin
from .import models
# Register your models here.
admin.site.register(models.Admin)
admin.site.register(models.Login)
admin.site.register(models.ImageUpload)
admin.site.register(models.CardsUpload)
admin.site.register(models.Enquiry)