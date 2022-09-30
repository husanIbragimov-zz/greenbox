from rest_framework import generics
from .serializers import MissionAndVisionSerializer
from apps.mission_vision.models import MissionAndVision


class MissionAndVisionListAPIView(generics.ListAPIView):
    queryset = MissionAndVision.objects.filter(is_active=True).order_by('-id')
    serializer_class = MissionAndVisionSerializer
    pagination_class = None


class MissionAndVisionRetrieveAPIView(generics.RetrieveAPIView):
    queryset = MissionAndVision.objects.all()
    serializer_class = MissionAndVisionSerializer
    lookup_field = 'pk'

