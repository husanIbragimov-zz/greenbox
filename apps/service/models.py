from django.db import models
from apps.company.models import Background
from django.utils.translation import gettext_lazy as _


SERVICE = (
    (0, _('Legal advice')),
    (1, _('Starting Business')),
)


class Service(models.Model):
    service = models.IntegerField(choices=SERVICE, default=0)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='service/images/')
    background = models.ForeignKey(Background, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



