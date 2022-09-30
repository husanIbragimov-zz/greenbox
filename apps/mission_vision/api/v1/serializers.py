from rest_framework import serializers
from apps.mission_vision.models import MissionAndVision


class MissionAndVisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionAndVision
        fields = ('id', 'title', 'image', 'description')
