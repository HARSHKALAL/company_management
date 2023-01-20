from django.urls import path
from .api import CompanyApi

urlpatterns = [
    path("api/company/create",CompanyApi.as_view(),name='CompanyApi'),
]