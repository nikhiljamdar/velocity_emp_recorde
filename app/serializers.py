from rest_framework import serializers
from .models import Employee,PhoneNumber
from rest_framework.serializers import Serializer, CharField

class UserRegistrationSerializer(Serializer):
    username = CharField(required=True)
    password = CharField(required=True)

class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model=PhoneNumber
        fields = ['id', 'number']

class EmployeeSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberSerializer(read_only=True)  

    class Meta:
        model = Employee
        fields = ['id', 'name','salary','email', 'phone_number']
