from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from apiV1.models import Employee2
from apiV1.serializers import Employee2Serializer

# Create your views here.


class Employee2ViewSet(viewsets.ModelViewSet):
    queryset = Employee2.objects.all()
    serializer_class = Employee2Serializer
