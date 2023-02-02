from .models import AuditLog
from .models import *
from django.contrib.contenttypes.models import ContentType


def create_audit_log_of_company(data):
    print(data.values())
    company_object = Company.objects.get(id=int(data.get('id')))
    model_name = company_object.__class__.__name__.lower()
    app_name = company_object._meta.app_label
    content_type = ContentType.objects.get(app_label=app_name, model=model_name)
    AuditLog.objects.create(
        content_type_id=content_type, object_id=company_object.id, log_message="Updated Successfully"
    )


def delete_data(get_ids):
    Company.objects.filter(id__in=get_ids).delete()
