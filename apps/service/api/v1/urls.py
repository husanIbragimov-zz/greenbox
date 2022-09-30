from django.urls import path
from .views import ServiceListAPIView, ServiceRetrieveAPIView

urlpatterns = [
    path('business-consolting/', ServiceListAPIView.as_view()),
    path('business-consolting/<int:pk>/', ServiceRetrieveAPIView.as_view()),
]
