from modeltranslation.translator import translator, TranslationOptions
from apps.work.models import Work, Category, Visa, Job


class WorkTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'background')


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


class VisaTranslationOptions(TranslationOptions):
    fields = ('category', 'background', 'title', 'description')


class JobTranslationOptions(TranslationOptions):
    fields = ('title', 'salary', 'industry')


translator.register(Work, WorkTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Visa, VisaTranslationOptions)
translator.register(Job, JobTranslationOptions)
