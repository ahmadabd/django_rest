from django.shortcuts import render
from .models import Employees
from .serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class EmployeeList(APIView):

    def get(self, request):
        employees1 = Employees.objects.all()
        serializer = EmployeeSerializer(employees1, many = True)
        return Response(serializer.data)

    def post(self):
        pass
