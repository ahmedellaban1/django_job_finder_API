from rest_framework import generics, status
from rest_framework.response import Response
from .models import Job
from .serializers import JobSerializer
from rest_framework.decorators import api_view
from etc.response_errors import ERORR_404
from django.shortcuts import get_object_or_404

class JobListView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

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

