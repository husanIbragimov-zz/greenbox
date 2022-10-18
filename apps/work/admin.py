from django.contrib import admin
from apps.work.models import Category, Work, ExpertiseLevel, WorkingConditionAndBenefit, Job, Specialty, Framework, \
    ProgrammingLanguages, JobType, WorkVisa,InternVisa
from modeltranslation.admin import TranslationAdmin


class WorkAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'is_active')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')


class VisaAdmin(TranslationAdmin):
    list_display = ('title', 'created_at', 'is_active')


class InternVisaAdmin(TranslationAdmin):
    list_display = ('title', 'created_at', 'is_active')


class JobAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'industry', 'speciality', 'is_active')
    filter_horizontal = ('frameworks', 'working_conditions_and_benefits')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(WorkVisa, VisaAdmin)
admin.site.register(InternVisa, InternVisaAdmin)
admin.site.register(JobType)
admin.site.register(ProgrammingLanguages)
admin.site.register(Specialty)
admin.site.register(Framework)
admin.site.register(ExpertiseLevel)
admin.site.register(WorkingConditionAndBenefit)
admin.site.register(Job, JobAdmin)
