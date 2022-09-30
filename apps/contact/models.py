from django.db import models
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    DEPARTMENT = (
        (0, _('None')),
        (1, _('University')),
        (2, _('Work')),
        (3, _('Study')),
        (4, _('Order')),
    )

    STATUS = (
        (0, _('NEW')),
        (1, _('PROCESS')),
        (2, _('CANCELED')),
        (3, _('FINISHED')),
    )

    class Meta:
        verbose_name = "Let's talk"
        verbose_name_plural = "1. Let's talk"

    name = models.CharField(max_length=50)
    email = models.EmailField()
    department = models.IntegerField(choices=DEPARTMENT, default=0)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
