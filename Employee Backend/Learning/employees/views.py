from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse
from employees.models import Employee

def employee_details(request, pk):
    # employee = get_object_or_404(Employee, pk=pk)
    # print(employee)
    # return HttpResponse(employee)


    try:
        employee = Employee.objects.get(pk=pk)
        print(employee)
        # return HttpResponse(employee)
        context ={
            'employee': employee,
        }
        return render(request, "employeeDetails.html", context)
    except:
        raise Http404

