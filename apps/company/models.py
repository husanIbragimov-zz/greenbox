from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Background(models.Model):
    STATUS = (
        (0, 'NONE'),
        (1, 'TOP'),
        (2, 'MIDDLE'),
        (3, 'BOTTOM'),
    )

    class Meta:
        verbose_name = 'Backgrounds'
        verbose_name_plural = '1. Backgrounds'

    title = models.CharField(max_length=100)
    background = models.ImageField(upload_to='background/', verbose_name=_('Background'))
    status = models.IntegerField(choices=STATUS, default=0, verbose_name=_('Status'))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'


class Article(models.Model):
    class Meta:
        verbose_name = 'Articles'
        verbose_name_plural = '2. Articles'

    title = models.CharField(max_length=100, verbose_name=_('Article title'))
    image = models.ImageField(upload_to='company/article-image/', null=True, verbose_name=_('Image'))
    background = models.ForeignKey(Background, on_delete=models.CASCADE, null=True)
    description = models.TextField(verbose_name=_('Description'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class About(models.Model):
    class Meta:
        verbose_name = 'About company'
        verbose_name_plural = '3. About company'

    title = models.CharField(max_length=100, verbose_name=_('About title'))
    image = models.ImageField(upload_to='about/image/', null=True, verbose_name=_('Image'))
    background = models.ForeignKey(Background, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    def __str__(self):
        return self.title


class Brand(models.Model):
    class Meta:
        verbose_name = 'Brands'
        verbose_name_plural = '4. Brands'

    title = models.CharField(max_length=100, verbose_name=_('Brand title'))
    image = models.ImageField('brand/images/')
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    def __str__(self):
        return self.image.url


class Certificate(models.Model):
    class Meta:
        verbose_name = 'Certificates'
        verbose_name_plural = '5. Certificates'

    title = models.CharField(max_length=100, verbose_name=_('Certificate title'))
    description = models.TextField()
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    def __str__(self):
        return self.title


class CertificateImage(models.Model):
    certificate = models.ForeignKey(Certificate, on_delete=models.SET_NULL, null=True,
                                    related_name='certificate_images')
    image = models.ImageField(upload_to='certificate/images/')
    is_active = models.BooleanField(default=True)

    @property
    def get_image_url(self):
        if settings.DEBUG:
            return f"{settings.LOCAL_BASE_URL}{self.image.url}"
        else:
            return f"{settings.PROD_BASE_URL}{self.image.url}"

    def __str__(self):
        return f'Image of {self.certificate.id}'
