from modeltranslation.translator import translator, TranslationOptions
from apps.work.models import Work, Category, WorkVisa, InternVisa, Job


class WorkTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'background')


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


class WorkVisaTranslationOptions(TranslationOptions):
    fields = ('background', 'title', 'description')


class InternVisaTranslationOptions(TranslationOptions):
    fields = ('background', 'title', 'description')


class JobTranslationOptions(TranslationOptions):
    fields = ('title', 'salary', 'industry')


translator.register(Work, WorkTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(WorkVisa, WorkVisaTranslationOptions)
translator.register(InternVisa, InternVisaTranslationOptions)
translator.register(Job, JobTranslationOptions)
