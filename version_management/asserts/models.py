from django.db import models

class Company(models.Model):
    name=models.CharField(max_length=100)
    ceo_name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Car(models.Model):
    name=models.CharField(max_length=30)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    color=models.CharField(max_length=20)
    mileage=models.IntegerField()
    unit=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    launch_year=models.DateField()

    def __str__(self):
        return self.name