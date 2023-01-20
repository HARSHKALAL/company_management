from .models import Company
from rest_framework import serializers

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("name","ceo_name")

    def create(self, validated_data):
        company = Company.objects.create(
            name=validated_data['name'],
            ceo_name = validated_data['ceo_name']
        )
        return company

# class CompanyListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Company




