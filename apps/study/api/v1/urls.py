from django.urls import path
from .views import CategoryListAPIView, StudyListAPIView, StudyBlogRetrieveAPIView, StudyBlogListAPIView, \
    UniversityRetrieveAPIView, UniversityFilterAPIView, UniversityListAPIView

urlpatterns = [
    path('category/', CategoryListAPIView.as_view()),
    path('study-blogs/', StudyBlogListAPIView.as_view()),
    path('study-blog/<int:pk>/', StudyBlogRetrieveAPIView.as_view()),
    path('university/', UniversityListAPIView.as_view()),
    path('university/<int:pk>/', UniversityRetrieveAPIView.as_view()),
    path('university-search/', UniversityFilterAPIView.as_view()),
]
