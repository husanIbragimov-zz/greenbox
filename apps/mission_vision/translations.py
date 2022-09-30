from modeltranslation.translator import translator, TranslationOptions
from apps.mission_vision.models import MissionAndVision


class MissionAndVisionTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(MissionAndVision, MissionAndVisionTranslationOptions)
