from modeltranslation.translator import translator, TranslationOptions
from apps.service.models import Service


class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'background', 'description')


translator.register(Service, ServiceTranslationOptions)
