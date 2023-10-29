from django.shortcuts import render
from rest_framework import generics, status
from .models import Job, Category, Company
from .serializers import JobSerializer


class JobListView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

job_list = JobListView.as_view()