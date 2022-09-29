from django.urls import path
from . import views

urlpatterns = [
    path('banner/', views.ArticleBannerListAPIView.as_view()),
    path('banner/<int:pk>/', views.ArticleBannerRetrieveAPIView.as_view()),
    path('background/', views.BackgroundListAPIView.as_view()),
    path('background/<int:pk>/', views.BackgroundRetrieveAPIView.as_view()),
    path('blogs/', views.ArticleListAPIView.as_view()),
    path('blog/<int:pk>/', views.ArticleRetrieveAPIView.as_view()),
    path('search/', views.SearchArticleListAPIView.as_view()),
    path('company-brands/', views.BrandListAPIView.as_view()),
    path('company-brand/<int:pk>/', views.BrandRetrieveAPIView.as_view()),
    path('certificate/', views.CertificateListAPIView.as_view()),
]
