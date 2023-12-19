from django.shortcuts import render
from rest_framework import viewsets

from django.http import HttpResponse

from django.apps import apps
from .serializers import Employee2Serializer, Role2Serializer, Department2Serializer
from .models import Employee2, Role2, Department2
# from django.db import models


class Employee2ViewSet(viewsets.ModelViewSet):
    queryset = Employee2.objects.all()
    serializer_class = Employee2Serializer


class Role2ViewSet(viewsets.ModelViewSet):
    queryset = Role2.objects.all()
    serializer_class = Role2Serializer


class Department2ViewSet(viewsets.ModelViewSet):
    queryset = Department2.objects.all()
    serializer_class = Department2Serializer


def index(request):
    # objects = MyModel.objects.all()
    return HttpResponse('Welcome')
