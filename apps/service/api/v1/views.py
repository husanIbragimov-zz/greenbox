from django.db.models import Q
from rest_framework import generics
from apps.service.models import Service
from .serializers import ServiceSerializer


class ServiceListAPIView(generics.ListAPIView):
    queryset = Service.objects.filter(is_active=True).order_by('-id')
    serializer_class = ServiceSerializer

    def get_queryset(self):
        qs = self.queryset.all()
        query = self.request.GET.get('q')
        query__in = Q()
        if query:
            query__in = Q(service__in=query)
        qs = qs.filter(query__in)
        return qs


class ServiceRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
