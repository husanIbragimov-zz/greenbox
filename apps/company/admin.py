from django.contrib import admin
from apps.company.models import About, Article, Brand, Background, CertificateImage, Certificate
from modeltranslation.admin import TranslationAdmin


class BackgroundAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'status')


class ArticleAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'updated_at', 'created_at', 'is_active')
    list_filter = ('updated_at', 'created_at')
    search_fields = ('id', 'title', 'description')
    readonly_fields = ('updated_at', 'created_at')


class AboutAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'created_at', 'is_active')
    list_filter = ('created_at',)
    search_fields = ('id', 'title', 'description')


class BrandAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'created_at', 'is_active')


class CertificateImageInline(admin.TabularInline):
    model = CertificateImage
    extra = 1


class CertificateAdmin(TranslationAdmin):
    inlines = [CertificateImageInline]
    list_display = ('id', 'title', 'created_at', 'is_active')
    readonly_fields = ('created_at',)


admin.site.register(About, AboutAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Background, BackgroundAdmin)
admin.site.register(Certificate, CertificateAdmin)
