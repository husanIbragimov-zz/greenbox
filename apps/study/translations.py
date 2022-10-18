from modeltranslation.translator import translator, TranslationOptions
from apps.study.models import Category, Study, StudyBlog, University


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


class StudyTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'background')


class StudyBlogTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class UniversityTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(Category, CategoryTranslationOptions)
translator.register(Study, StudyTranslationOptions)
translator.register(StudyBlog, StudyBlogTranslationOptions)
translator.register(University, UniversityTranslationOptions)

