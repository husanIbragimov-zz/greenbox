from django.db import models


class Contact(models.Model):
    DEPARTMENT = (
        (0, 'None'),
        (1, 'University'),
        (2, 'Work'),
        (3, 'Study'),
        (4, 'Order'),
    )

    STATUS = (
        (0, 'NEW'),
        (1, 'PROCESS'),
        (2, 'CANCELED'),
        (3, 'FINISHED'),
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
