# Generated by Django 4.1.5 on 2023-01-31 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asserts', '0006_alter_auditlog_ip_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auditlog',
            name='created_by',
        ),
    ]
