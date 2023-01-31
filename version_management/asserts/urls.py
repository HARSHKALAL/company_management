from django.urls import path
from .api import CompanyApi, CarApi, AuditLogViewSet
from .views import *

urlpatterns = [
    path("homepage/", homepage, name="homepage"),
    path("company_list/", company_list, name="company_list"),
    path("car_list/", car_list, name="car_list"),


    path("api/company/", CompanyApi.as_view({"get":"list"}), name='CompanyApi'),
    path("api/company/retrieve/<int:pk>/", CompanyApi.as_view({"post": "retrieve"}), name='CompanyApi'),
    path("api/company/update/<int:pk>/", CompanyApi.as_view({"put": "update"}), name='CompanyApi'),
    path("api/car/", CarApi.as_view(), name='CarApi'),
    path("api/audit_log/", AuditLogViewSet.as_view({'post': 'list'}), name='AuditLogViewSet'),



]