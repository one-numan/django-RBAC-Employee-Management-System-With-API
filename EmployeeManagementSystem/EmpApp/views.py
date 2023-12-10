from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Employee, Role, Department
from django.db.models import Q
# Create your views here.


def index(request):
    return render(request, 'index.html')


def fetch_all_emp(emps=None):
    if not emps:
        emps = Employee.objects.all()

    context = {
        'emps': emps
    }
    return context


def all_emp(request):
    return render(request, 'all_emp.html', context=fetch_all_emp())


def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        new_emp = Employee(first_name=first_name, last_name=last_name,
                           salary=salary, bonus=bonus, role_id=role, dept_id=dept)
        new_emp.save()
        return HttpResponse("Form Submitted")
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return render(request, "Something Went Wrong")


def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            deletion_emp = Employee.objects.get(id=emp_id)
            deletion_emp.delete()
            return HttpResponse('Deletion Done')
        except:
            return HttpResponse('Something Went Wrong')
    return render(request, 'remove_emp.html', context=fetch_all_emp())


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name)
                               | Q(last_name__icontains=name))
            return render(request, 'all_emp.html', context=fetch_all_emp(emps=emps))
        else:
            return HttpResponse("Something Went Wrong")
    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse("Something Went Wrong")
