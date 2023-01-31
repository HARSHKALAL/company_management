from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.db.models import GenericIPAddressField
import socket


class Company(models.Model):
    """ This model is used to store Company details """
    name = models.CharField(max_length=100)
    ceo_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):
    """ This model is used to store Car details """
    name = models.CharField(max_length=30)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    color = models.CharField(max_length=20)
    mileage = models.IntegerField()
    unit = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    launch_year = models.DateField()

    def __str__(self):
        return self.name


class AuditLog(models.Model):
    content_type_id = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(null=True)
    log_message = models.CharField(max_length=500)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=35,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        hostname = socket.gethostname()
        self.ip_address = socket.gethostbyname(hostname)
        super(AuditLog, self).save(*args, **kwargs)
