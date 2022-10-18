from django.db.models import Q
from rest_framework import generics, permissions, filters
from apps.work.models import Category, Work, Specialty, WorkingConditionAndBenefit, Framework, Job, JobType, \
    ExpertiseLevel, ProgrammingLanguages, WorkVisa, InternVisa
from .serializers import CategorySerializer, WorkSerializer, JopTypeSerializers, ProgrammingLanguagesSerializer, \
    SpecialitySerializer, FrameworkSerializer, ExpertiseLevelSerializer, WorkingConditionAndBenefitSerializer, \
    JobSerializer, VisaSerializer


class WorkListAPIView(generics.ListAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class VisaListAPIView(generics.ListAPIView):
    queryset = WorkVisa.objects.filter(is_active=True).order_by('-id')
    serializer_class = VisaSerializer


class VisaRetrieveAPIView(generics.RetrieveAPIView):
    queryset = WorkVisa.objects.all()
    serializer_class = VisaSerializer
    lookup_field = 'pk'


class InternVisaListAPIView(generics.ListAPIView):
    queryset = InternVisa.objects.filter(is_active=True).order_by('-id')
    serializer_class = VisaSerializer


class InternVisaRetrieveAPIView(generics.RetrieveAPIView):
    queryset = InternVisa.objects.all()
    serializer_class = VisaSerializer
    lookup_field = 'pk'


class JobTypeListAPIView(generics.ListAPIView):
    queryset = JobType.objects.filter(is_active=True).order_by('-id')
    serializer_class = JopTypeSerializers
    pagination_class = None


class JobTypeRetrieveAPIView(generics.RetrieveAPIView):
    queryset = JobType.objects.all()
    serializer_class = JopTypeSerializers
    lookup_field = 'pk'


class ProgrammingLanguagesListAPIView(generics.ListAPIView):
    queryset = ProgrammingLanguages.objects.filter(is_active=True).order_by('-id')
    serializer_class = ProgrammingLanguagesSerializer
    pagination_class = None


class ProgrammingLanguagesRetrieveAPIView(generics.RetrieveAPIView):
    queryset = ProgrammingLanguages.objects.all()
    serializer_class = ProgrammingLanguagesSerializer
    lookup_field = 'pk'


class SpecialtyListAPIView(generics.ListAPIView):
    queryset = Specialty.objects.filter(is_active=True).order_by('-id')
    serializer_class = SpecialitySerializer
    pagination_class = None


class SpecialtyRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Specialty.objects.all()
    serializer_class = SpecialitySerializer
    lookup_field = 'pk'


class FrameworkListAPIView(generics.ListAPIView):
    queryset = Framework.objects.filter(is_active=True).order_by('-id')
    serializer_class = FrameworkSerializer
    pagination_class = None


class FrameworkRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Framework.objects.all()
    serializer_class = FrameworkSerializer
    lookup_field = 'pk'


class ExpertiseLevelListAPIView(generics.ListAPIView):
    queryset = ExpertiseLevel.objects.filter(is_active=True).order_by('-id')
    serializer_class = ExpertiseLevelSerializer
    pagination_class = None


class ExpertiseLevelRetrieveAPIView(generics.RetrieveAPIView):
    queryset = ExpertiseLevel.objects.all()
    serializer_class = ExpertiseLevelSerializer
    lookup_field = 'pk'


class WorkingConditionAndBenefitListAPIView(generics.ListAPIView):
    queryset = WorkingConditionAndBenefit.objects.filter(is_active=True).order_by('-id')
    serializer_class = WorkingConditionAndBenefitSerializer
    pagination_class = None


class WorkingConditionAndBenefitRetrieveAPIView(generics.RetrieveAPIView):
    queryset = WorkingConditionAndBenefit.objects.all()
    serializer_class = WorkingConditionAndBenefitSerializer
    lookup_field = 'pk'


class JobListAPIView(generics.ListAPIView):
    queryset = Job.objects.filter(is_active=True).order_by('-id')
    serializer_class = JobSerializer


class JobRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (permissions.AllowAny,)
    lookup_field = 'pk'


class JobFilterListAPIView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    pagination_class = None

    def get_queryset(self, *args, **kwargs):
        queryset_list = super().get_queryset().filter(is_active=True)
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(jop_type__title__icontains=query) |
                Q(speciality__title__icontains=query) |
                Q(frameworks__title__icontains=query) |
                Q(programming_language__title__icontains=query) |
                Q(working_conditions_and_benefits__title__icontains=query)
            )
        return queryset_list
