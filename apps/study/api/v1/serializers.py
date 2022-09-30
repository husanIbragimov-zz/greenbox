from rest_framework import serializers
from apps.study.models import Category, Study, StudyBlog, University, UniversityImages


class CategoryStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title',)


class StudySerializer(serializers.ModelSerializer):
    class Meta:
        model = Study
        fields = ('id', 'title', 'image', 'background_image', 'description')


class StudyBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyBlog
        fields = (
            'id',
            'category',
            'title',
            'image',
            'background',
            'description',
        )


class UniversityImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityImages
        fields = ('id', 'image')


class UniversitySerializer(serializers.ModelSerializer):
    university_images = UniversityImagesSerializer(many=True)

    class Meta:
        model = University
        fields = (
            'id',
            'title',
            'background',
            'description',
            'university_images',
        )
