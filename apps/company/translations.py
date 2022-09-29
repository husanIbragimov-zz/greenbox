from modeltranslation.translator import TranslationOptions, translator
from apps.company.models import Background, Article, About, Brand, Certificate


# @register(Background)
class BackgroundTranslationOptions(TranslationOptions):
    fields = ()


class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'background')


class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'background')


class BrandTranslationOptions(TranslationOptions):
    fields = ('title',)


class CertificateTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(Background, BackgroundTranslationOptions)
translator.register(Article, ArticleTranslationOptions)
translator.register(About, AboutTranslationOptions)
translator.register(Brand, BrandTranslationOptions)
translator.register(Certificate, CertificateTranslationOptions)
