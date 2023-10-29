from django.urls import path
from .views import job_list, job_details

urlpatterns = [
    path('', job_list, name='job_list_API_view'),
    path('<int:id>', job_details, name='job_details_API_view')
]