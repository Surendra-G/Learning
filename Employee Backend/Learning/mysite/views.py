from django.http import HttpResponse
from django.shortcuts import render
from employees.models import Employee

def home(resquest):
    employees = Employee.objects.all()
    print(employees)
    context = {
        'employees': employees,
    }
    return render(resquest, 'home.html',context)
