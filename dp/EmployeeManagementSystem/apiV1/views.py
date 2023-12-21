# from django.shortcuts import render
from rest_framework import viewsets
# from rest_framework.permissions import AllowAny
from apiV1.models import Employee2, Role2, Department2
from apiV1.serializers import Employee2Serializer, Role2Serializer, Department2Serializer

# Create your views here.


class Employee2ViewSet(viewsets.ModelViewSet):
    queryset = Employee2.objects.all()
    serializer_class = Employee2Serializer


class Role2ViewSet(viewsets.ModelViewSet):
    queryset = Role2.objects.all()
    serializer_class = Role2Serializer


class Department2ViewSet(viewsets.ModelViewSet):
    queryset = Department2.objects.all()
    serializer_class = Department2Serializer
