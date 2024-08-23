from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'v3_index.html')
    # return HttpResponse('Welcome Version 4')


def home(request):
    return HttpResponse('Home Page')


def add(request):
    return HttpResponse('Add Page')
