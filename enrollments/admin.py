from django.contrib import admin
from .models import Enrollment, Progress

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'course', 'enrolled_at', 'is_active']
    list_filter = ['is_active']

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ['id', 'enrollment', 'module', 'completed', 'completed_at']
    list_filter = ['completed']
