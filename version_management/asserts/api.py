from rest_framework.views import APIView, Response
from .serializers import CompanySerializer, CarSerializer, AuditLogSerializer
from rest_framework import generics, status
from .models import Company, Car, AuditLog
from rest_framework import viewsets
from .utils import delete_data
from .utils import create_audit_log_of_company, delete_data
from rest_framework.permissions import IsAuthenticated


class CompanyApi(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    def update(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        get_ids = request.data.getlist('ids[]')
        delete_data(get_ids)
        return Response({"message": "Delete Successfully"})


class CarApi(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class AuditLogViewSet(viewsets.ModelViewSet):
    serializer_class = AuditLogSerializer
    queryset = AuditLog.objects.all()
