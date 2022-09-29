from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.service.api.v1.urls')),
]
