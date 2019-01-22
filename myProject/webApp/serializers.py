from rest_framework import serializers
from .models import Employees

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('firstName', 'lastName')
        #fields = '__all__'       means all model fields  


