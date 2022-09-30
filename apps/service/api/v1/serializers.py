from rest_framework import serializers
from apps.service.models import Service


class ServiceSerializer(serializers.ModelSerializer):
    service_display = serializers.SerializerMethodField(read_only=True)

    def get_service_display(self, obj):
        return obj.get_service_display()

    class Meta:
        model = Service
        fields = ('id',
                  'service',
                  'service_display',
                  'title', 'image',
                  'background',
                  'description')
