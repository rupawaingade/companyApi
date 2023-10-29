from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company
from api.models import Employee
from api.serializers import CompanySerializers,EmployeeSerializer
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializers


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

