from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.visa.api.v1.urls')),
]
