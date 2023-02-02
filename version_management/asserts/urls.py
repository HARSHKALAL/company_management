from django.urls import path
from .api import CompanyApi, CarApi, AuditLogViewSet
from .views import *

urlpatterns = [
    path("homepage/", homepage, name="homepage"),
    path("company_list/", company_list, name="company_list"),
    path("car_list/", car_list, name="car_list"),

    path("api/company/", CompanyApi.as_view({"get": "list"}), name='CompanyApi'),
    path("api/company/retrieve/<int:pk>/", CompanyApi.as_view({"post": "retrieve"}), name='CompanyApi'),
    path("api/company/update/<int:pk>/", CompanyApi.as_view({"put": "update"}), name='CompanyApi'),
    path("api/company/delete/<int:pk>/", CompanyApi.as_view({'delete': 'destroy'}), name='CompanyApi'),

    path("api/car/", CarApi.as_view({"get": "list"}), name='CarApi'),
    path("api/car/retrieve/<int:pk>/", CarApi.as_view({"post": "retrieve"}), name='CarApi'),
    path("api/car/update/<int:pk>/", CarApi.as_view({"put": "update"}), name='CarApi'),
    # path("api/company/create/<int:pk>/", AuditLogViewSet.as_view(), name='AuditLogViewSet'),

]