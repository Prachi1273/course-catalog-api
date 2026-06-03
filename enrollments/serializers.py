from rest_framework import serializers
from .models import Enrollment, Progress
from courses.serializers import CourseSerializer


class EnrollmentSerializer(serializers.ModelSerializer):
    course_detail = CourseSerializer(source='course', read_only=True)

    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'course', 'course_detail', 'enrolled_at', 'is_active']
        read_only_fields = ['student', 'enrolled_at']


class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ['id', 'enrollment', 'module', 'completed', 'completed_at']
        read_only_fields = ['enrollment']