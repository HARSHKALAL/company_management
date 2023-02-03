from rest_framework.views import APIView, Response
from .serializers import CompanySerializer, CarSerializer, AuditLogSerializer
from rest_framework import generics, status
from .models import Company, Car, AuditLog
from rest_framework import viewsets
from .utils import delete_data
from .utils import create_audit_log, delete_data
from rest_framework.permissions import IsAuthenticated
from django.db import transaction


class CompanyApi(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    def update(self, request, *args, **kwargs):
        log_messages = {'message': 'Company Data Update Successfully'}
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        company_object = Company.objects.filter(id=kwargs.get('pk'))
        create_audit_log(company_object, log_messages)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)

    @transaction.atomic()
    def destroy(self, request, *args, **kwargs):
        log_messages = {'message': 'Company Data Delete Successfully'}
        get_ids = request.data.getlist('ids[]')
        company_object = Company.objects.filter(id__in=get_ids)
        create_audit_log(company_object, log_messages)
        delete_data(get_ids)
        return Response({"message": "Delete Successfully"})


class CarApi(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class AuditLogViewSet(viewsets.ModelViewSet):
    serializer_class = AuditLogSerializer
    queryset = AuditLog.objects.all()
