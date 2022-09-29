from django.db.models import Q
from rest_framework import generics
from apps.company.models import Brand, Background, About, Article, Certificate
from .serializers import BackgroundSerializer, ArticleSerializer, AboutSerializer, BrandSerializer, \
    CertificateSerializer


class BackgroundListAPIView(generics.ListAPIView):
    queryset = Background.objects.all()
    serializer_class = BackgroundSerializer


class BackgroundRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Background.objects.all()
    serializer_class = BackgroundSerializer
    lookup_field = 'pk'


class ArticleListAPIView(generics.ListAPIView):
    queryset = Article.objects.filter(is_active=True).order_by('-id')[1:]
    serializer_class = ArticleSerializer


class ArticleBannerListAPIView(generics.ListAPIView):
    queryset = Article.objects.filter(is_active=True).order_by('-id')[:1]
    serializer_class = ArticleSerializer
    pagination_class = None


class ArticleBannerRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'pk'


class SearchArticleListAPIView(generics.ListAPIView):
    queryset = Article.objects.filter(is_active=True).order_by('-id')
    serializer_class = ArticleSerializer

    def get_queryset(self):
        qs = self.queryset.all()
        search = self.request.GET.get('search')

        search_condition = Q()
        if search:
            search_condition = (Q(title__icontains=search) | Q(description__icontains=search))
        qs = qs.filter(search_condition)
        return qs


class AboutUsListAPIView(generics.ListAPIView):
    queryset = About.objects.filter(is_active=True).order_by('-id')[:1]
    serializer_class = AboutSerializer


class BrandListAPIView(generics.ListAPIView):
    queryset = Brand.objects.filter(is_active=True).order_by('-id')
    serializer_class = BrandSerializer
    lookup_field = 'pk'


class BrandRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CertificateListAPIView(generics.ListAPIView):
    queryset = Certificate.objects.filter(is_active=True).order_by('-id')
    serializer_class = CertificateSerializer
