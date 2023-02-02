from .models import Company, Car, AuditLog
from rest_framework import serializers
from .models import *
from django.contrib.contenttypes.models import ContentType


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("id", "name", "ceo_name")


class CarSerializer(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = ("id", "name",  "company_name", "color", "mileage", "unit", "price", "launch_year")

    @staticmethod
    def get_company_name(instance):
        return instance.company.name


class AuditLogSerializer(serializers.ModelSerializer):
    # content_type_id = serializers.SerializerMethodField()
    class Meta:
        model = AuditLog
        fields = ("content_type_id", "object_id", "log_message")










    # def get_content_type_id(self, instance):
        # app_label_query = ContentType.objects.get_for_id(instance.content_type_id)
        # return instance.content_type_id.model
