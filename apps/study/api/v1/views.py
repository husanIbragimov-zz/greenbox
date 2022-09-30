from django.db.models import Q
from rest_framework import generics
from apps.study.models import Category, Study, StudyBlog, University
from .serializers import CategoryStudySerializer, StudySerializer, StudyBlogSerializer, UniversitySerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryStudySerializer
    pagination_class = None


class StudyListAPIView(generics.ListAPIView):
    queryset = Study.objects.filter(is_active=True).order_by('-id')
    serializer_class = StudySerializer
    pagination_class = None


class StudyBlogListAPIView(generics.ListAPIView):
    queryset = StudyBlog.objects.filter(is_active=True).order_by('-id')
    serializer_class = StudyBlogSerializer


class StudyBlogRetrieveAPIView(generics.RetrieveAPIView):
    queryset = StudyBlog.objects.all()
    serializer_class = StudyBlogSerializer
    lookup_field = 'pk'


class UniversityListAPIView(generics.ListAPIView):
    queryset = University.objects.filter(is_active=True).order_by('-id')
    serializer_class = UniversitySerializer


class UniversityFilterAPIView(generics.ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

    def get_queryset(self):
        qs = self.queryset.filter(is_active=True).order_by('-id')
        query = self.request.GET.get('q')

        query_condition = Q()
        if query:
            query_condition = (Q(title__icontains=query) | Q(description__icontains=query))
        qs = qs.filter(query_condition)
        return qs


class UniversityRetrieveAPIView(generics.RetrieveAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    lookup_field = 'pk'
