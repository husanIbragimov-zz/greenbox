from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.work.api.v1.urls')),
]
