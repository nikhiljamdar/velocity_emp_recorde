from django.db import models

class PhoneNumber(models.Model):
    number=models.CharField(max_length=15)

    def __str__(self):
        return self.number

class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    salary=models.DecimalField(max_digits=10,decimal_places=2)
    phone_number=models.ForeignKey(PhoneNumber,on_delete=models.CASCADE)

    def __str__(self):
        return self.name