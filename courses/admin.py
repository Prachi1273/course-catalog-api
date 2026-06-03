from django.contrib import admin
from .models import Category, Course, Module

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'instructor', 'category', 'price', 'level', 'created_at']
    list_filter = ['level', 'category']
    search_fields = ['title', 'description']

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'course', 'order']
    list_filter = ['course']