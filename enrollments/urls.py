from django.urls import path
from . import views

urlpatterns = [
    path('', views.EnrollmentListCreateView.as_view(), name='enrollment-list'),
    path('modules/<int:module_id>/complete/', views.mark_module_complete, name='mark-complete'),
]