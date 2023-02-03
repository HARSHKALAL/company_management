from .models import AuditLog
from .models import *
from django.contrib.contenttypes.models import ContentType


def create_audit_log(get_data, log_messages):
    for data in get_data:
        model_name = data.__class__.__name__.lower()
        app_name = data._meta.app_label
        content_type = ContentType.objects.get(app_label=app_name, model=model_name)
        AuditLog.objects.create(
            content_type_id=content_type, object_id=data.id, log_message=log_messages.get('message')
        )


def delete_data(get_ids):
    Company.objects.filter(id__in=get_ids).delete()
