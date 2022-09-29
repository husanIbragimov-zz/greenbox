from django.urls import path
from . import views


urlpatterns = [
    path('contact-us/', views.ContactCreateAPIView.as_view())
]
