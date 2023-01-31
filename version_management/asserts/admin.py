from django.contrib import admin
from .models import Company, Car, AuditLog
from django.contrib.contenttypes.models import ContentType


admin.site.register(Company)
admin.site.register(AuditLog)
admin.site.register(Car)
admin.site.register(ContentType)
