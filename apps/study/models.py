from django.conf import settings
from django.db import models
from apps.company.models import Background


class Category(models.Model):
    class Meta:
        verbose_name = "Categories"
        verbose_name_plural = "1. Categories"

    title = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Study(models.Model):
    class Meta:
        verbose_name = "Study"
        verbose_name_plural = "2. Study"

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='study/base/', null=True)
    background = models.ForeignKey(Background, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class StudyBlog(models.Model):
    class Meta:
        verbose_name = "Study Blogs"
        verbose_name_plural = "3. Study Blogs"

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='study/images/', null=True, blank=True)
    background_image = models.ImageField(upload_to='study/base/', null=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class University(models.Model):
    class Meta:
        verbose_name = "Universities"
        verbose_name_plural = "4. Universities"

    title = models.CharField(max_length=100)
    background = models.ForeignKey(Background, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class UniversityImages(models.Model):
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null=True, related_name='university_images')
    image = models.ImageField(upload_to='study/universities/')
    is_active = models.BooleanField(default=True)

    @property
    def get_image_url(self):
        if settings.DEBUG:
            return f"{settings.LOCAL_BASE_URL}{self.image.url}"
        else:
            return f"{settings.PROD_BASE_URL}{self.image.url}"

    def __str__(self):
        return f'Image of {self.university.id}'
