from django.contrib import admin
from apps.mission_vision.models import MissionAndVision
from modeltranslation.admin import TranslationAdmin


class MissionAndVisionAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'is_active', 'created_at')


admin.site.register(MissionAndVision, MissionAndVisionAdmin)
