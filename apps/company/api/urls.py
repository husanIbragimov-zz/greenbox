from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.company.api.v1.urls')),
]
