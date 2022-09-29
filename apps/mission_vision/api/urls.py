from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.mission_vision.api.v1.urls')),
]
