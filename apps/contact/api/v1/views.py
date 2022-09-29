from rest_framework import generics
from apps.contact.models import Contact
from .serializers import ContactSerializer


class ContactCreateAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
