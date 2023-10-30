from rest_framework import generics, status
from rest_framework.response import Response
from .models import Job
from .serializers import JobSerializer
from rest_framework.decorators import api_view
from etc.response_errors import ERORR_404
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class JobListView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'vacancy', 'job_type', ]
    search_fields = ['title', 'vacancy', 'job_type','description']
    ordering_fields = ['id', 'title', 'vacancy', 'job_type','description']


job_list = JobListView.as_view()


@api_view(['GET'])
def job_details(request, *args, **kwargs):
    try:
        job = Job.objects.get(id=kwargs['id'])
        serializer = JobSerializer(job).data
        response = {
            "job": serializer
        }
        return Response(response, status=status.HTTP_200_OK)
    except:
        return Response(ERORR_404, status=status.HTTP_404_NOT_FOUND)

