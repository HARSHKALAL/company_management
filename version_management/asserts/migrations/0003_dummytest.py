# Generated by Django 4.1.5 on 2023-01-30 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asserts', '0002_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='DummyTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]