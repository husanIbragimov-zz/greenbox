from django.contrib import admin
from apps.service.models import Service
from modeltranslation.admin import TranslationAdmin


class ServiceAdmin(TranslationAdmin):
    pass


admin.site.register(Service, ServiceAdmin)
