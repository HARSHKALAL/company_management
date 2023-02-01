from rest_framework.views import APIView,Response
from .serializers import CompanySerializer, CarSerializer, AuditLogSerializer
from rest_framework import generics
from .models import Company, Car, AuditLog
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated


class CompanyApi(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    def update(self, request, *args, **kwargs):
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
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)



    # def post(self, request, *args, **kwargs):
    #     serializer = self.serializer_class
    #     if serializer.is_valid():
    #         compnay_obj = serializer.save()
    #         create_audit_log_of_company(compnay_obj.id)
    #     return self.create(request, *args, **kwargs)


class CarApi(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

    def update(self, request, *args, **kwargs):
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



class AuditLogViewSet(viewsets.ModelViewSet):
    serializer_class = AuditLogSerializer
    # queryset = AuditLog.objects.all()

    # def create(self, request, *args, **kwargs):
    #     print("Hello")
    #     serializer = self.get_serializer(data=request.data)
    #     print(serializer, "???")
    # #     serializer.is_valid(raise_exception=True)
    # #     self.perform_create(serializer)
    # #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #















