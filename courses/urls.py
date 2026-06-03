from django.urls import path
from . import views

urlpatterns = [
    path('', views.CourseListCreateView.as_view(), name='course-list'),
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list'),
    path('<int:course_id>/modules/', views.ModuleListCreateView.as_view(), name='module-list'),
]
