from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.CategoryListAPIView.as_view()),
    path('work/', views.WorkListAPIView.as_view()),
    # path('work/<int:pk>/', views.WorkRetrieveAPIView.as_view()),
    path('visas/', views.VisaListAPIView.as_view()),
    path('visa/<int:pk>/', views.VisaRetrieveAPIView.as_view()),
    path('jop-types/', views.JobTypeListAPIView.as_view()),
    # path('jop-type/<int:pk>/', views.JobTypeRetrieveAPIView.as_view()),
    path('programming-languages/', views.ProgrammingLanguagesListAPIView.as_view()),
    path('specialties/', views.SpecialtyListAPIView.as_view()),
    path('frameworks/', views.FrameworkListAPIView.as_view()),
    path('expertise-level/', views.ExpertiseLevelListAPIView.as_view()),
    path('working-conditions-and-benefits/', views.WorkingConditionAndBenefitListAPIView.as_view()),
    path('jobs/', views.JobListAPIView.as_view()),
    path('job/<int:pk>/', views.JobRetrieveAPIView.as_view()),
    path('filter-tags/', views.JobFilterListAPIView.as_view())
]
