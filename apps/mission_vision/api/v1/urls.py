from django.urls import path
from . import views

urlpatterns = [
    path('mission-vision/', views.MissionAndVisionListAPIView.as_view()),
    path('mission-vision/<int:pk>/', views.MissionAndVisionRetrieveAPIView.as_view())
]
