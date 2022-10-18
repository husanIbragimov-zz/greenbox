from rest_framework import serializers
from apps.work.models import Category, Work, ExpertiseLevel, Framework, JobType, WorkingConditionAndBenefit, Job, \
    Specialty, ProgrammingLanguages, WorkVisa, InternVisa


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ('id', 'title', 'image', 'background')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title',)


class VisaSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkVisa
        fields = (
            'id',
            'title',
            'image',
            'background_image',
            'description',
            'created_at'
        )


class InternSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternVisa
        fields = (
            'id',
            'title',
            'image',
            'background_image',
            'description',
            'created_at'
        )


class JopTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobType
        fields = ('id', 'title', 'icon')


class ProgrammingLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingLanguages
        fields = ('id', 'title')


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = ('id', 'title')


class FrameworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Framework
        fields = ('id', 'title')


class ExpertiseLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpertiseLevel
        fields = ('id', 'title')


class WorkingConditionAndBenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingConditionAndBenefit
        fields = ('id', 'title')


class JobSerializer(serializers.ModelSerializer):
    jop_type = JopTypeSerializers()
    speciality = SpecialitySerializer()
    programming_language = ProgrammingLanguagesSerializer()
    frameworks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    expertise_level = ExpertiseLevelSerializer()
    working_conditions_and_benefits = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Job
        fields = (
            'id',
            'title',
            'salary',
            'industry',
            'created_at',
            'jop_type',
            'speciality',
            'programming_language',
            'frameworks',
            'expertise_level',
            'working_conditions_and_benefits',
            'is_active'
        )
