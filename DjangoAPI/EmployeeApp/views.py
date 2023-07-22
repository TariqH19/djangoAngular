from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Department, Employees
from EmployeeApp.serializers import DepartmentSerializer,EmployeesSerializer 

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def departmentApi(request,id=0):
    if request.method=="GET":
        department = Department.objects.all()
        department_serializer = DepartmentSerializer(department, many=True)
        return JsonResponse(department_serializer.data,safe=False)
    
    elif request.method=="POST":
        department_data=JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method=="PUT":
        department_data=JSONParser().parse(request)
        department = Department.objects.get(DepartmentId=department_data['DepartmentId'])
        department_serializer = DepartmentSerializer(department,data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    
    elif request.method=="DELETE":
        department = Department.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Department Deleted successfully.", safe=False)
    
@csrf_exempt
def employeesApi(request,id=0):
    if request.method=="GET":
        employees = Employees.objects.all()
        employees_serializer = EmployeesSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data,safe=False)
    
    elif request.method=="POST":
        employees_data=JSONParser().parse(request)
        employees_serializer = EmployeesSerializer(data=employees_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method=="PUT":
        employees_data=JSONParser().parse(request)
        employees = Employees.objects.get(EmployeeId=employees_data['EmployeeId'])
        employees_serializer = EmployeesSerializer(employees,data=employees_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    
    elif request.method=="DELETE":
        employees = Employees.objects.get(EmployeeId=id)
        employees.delete()
        return JsonResponse("Department Deleted successfully.", safe=False)
    
@csrf_exempt
def SaveFile(request):
    file=request.FILES['uploadedFile']
    file_name = default_storage.save(file.name,file)
    
    return JsonResponse(file_name,safe=False)