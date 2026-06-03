from django.shortcuts import render

from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.utils import timezone
from .models import Enrollment, Progress
from .serializers import EnrollmentSerializer, ProgressSerializer
from courses.models import Module


class EnrollmentListCreateView(generics.ListCreateAPIView):
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Enrollment.objects.filter(student=self.request.user)

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def mark_module_complete(request, module_id):
    try:
        module = Module.objects.get(id=module_id)
        enrollment = Enrollment.objects.get(
            student=request.user,
            course=module.course
        )
        progress, created = Progress.objects.get_or_create(
            enrollment=enrollment,
            module=module
        )
        progress.completed = True
        progress.completed_at = timezone.now()
        progress.save()
        return Response({'message': 'Module marked as complete!'})
    except (Module.DoesNotExist, Enrollment.DoesNotExist):
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
