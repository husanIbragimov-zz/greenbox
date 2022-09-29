from rest_framework import serializers
from apps.company.models import Article, About, Brand, Background, Certificate, CertificateImage


class BackgroundSerializer(serializers.ModelSerializer):
    status_display = serializers.SerializerMethodField(read_only=True)

    def get_status_display(self, obj):
        return obj.get_lang_display()

    class Meta:
        model = Background
        fields = (
            'id',
            'title',
            'status',
            'status_display',
            'background',
        )


class ArticleSerializer(serializers.ModelSerializer):
    background = serializers.ImageField(source='background.background', read_only=True)

    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'image',
            'background',
            'description',
        )


class AboutSerializer(serializers.ModelSerializer):
    background = BackgroundSerializer()

    class Meta:
        model = About
        fields = (
            'id',
            'title',
            'background',
            'description',
        )


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'id',
            'title',
            'image',
        )


class CertificateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificateImage
        fields = ('id', 'image')


class CertificateSerializer(serializers.ModelSerializer):
    certificate_images = CertificateImageSerializer(many=True)

    class Meta:
        model = Certificate
        fields = (
            'id',
            'title',
            'description',
            'certificate_images'
        )
