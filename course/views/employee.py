from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from django_countries.fields import countries

from course.models.employee import Employee
from course.models.category import Category
from course.forms.employee import EmployeeForm

from course.models.category import Category


@login_required
def list_employees(request):
    template = "employees/list.html"
    employees = Employee.objects.all()
    categories = Category.objects.all()
    context = {"employees": employees, "list_employee_active": "active", "employee_show": "show",
               "employee_active": "active", "categories": categories}
    return render(request, template, context)


@login_required
def detail_employees(request, pk):
    if request.user.is_superuser:
        template = "employees/details.html"
        employee = get_object_or_404(Employee, pk=pk)
        context = {"employee": employee}
        return render(request, template, context)
    else:
        raise PermissionDenied("You Are Not An Admin\nPermission Denied")


@login_required
def add_employee(request, input_data=None):
    template = "employees/add.html"
    form = EmployeeForm()
    categories = Category.objects.all()
    context = {"form": form, "input_data":input_data, "categories": categories, "add_employee_active": "active", "employee_show": "show",
               "employee_active": "active", "countries": countries}
    if input_data is not None:
        input_country = input_data.data.get("country")
        # import pdb; pdb.set_trace()
        for country in countries:
            if country[0] == input_country:
                country_input_name = country[1]
                country_input_code = country[0]
                context['country_input_name'] = country_input_name
                context['country_input_code'] = country_input_code 

        input_category = input_data.data.get("category")
        # import pdb; pdb.set_trace()
        category = Category.objects.get(pk=input_category)
        context['category'] = category
        
        input_sex = input_data.data.get("sex")
        context['sex'] = input_sex
        # import pdb; pdb.set_trace()
    return render(request, template, context)


@login_required
def create_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        # import pdb; pdb.set_trace()
        if form.is_valid():
            form.save()
            messages.success(request, "Employee Added Successfully")
            return redirect("list_employees")
        else:
            messages.error(request, "Employee Creation Failed!")
            return add_employee(request, form) # redirect("add_employee")


@login_required
def edit_employee(request, pk):
    # import pdb; pdb.set_trace()
    if request.user.is_superuser:
        template = "employees/edit.html"
        employee = get_object_or_404(Employee, pk=pk)
        # employee.trip_set.count()
        form = EmployeeForm(request.GET or None, instance=employee)
        country_edit_code = employee.country.code 
        selected_category = employee.category
        categories = Category.objects.all()
        sex = employee.sex
        context = {"form": form, "countries": countries, "country_edit_code": country_edit_code, "categories": categories, "sex": sex, "pk": pk}
        return render(request, template, context)
    else:
        raise PermissionDenied("You Are Not An Admin\nPermission Denied")


@login_required
def update_employee(request, pk):
    # import pdb; pdb.set_trace()
    if request.user.is_superuser:
        if request.method == "POST":
            employee = get_object_or_404(Employee, pk=pk)
            form = EmployeeForm(request.POST or None, instance=employee)
            # import pdb; pdb.set_trace()
            if form.is_valid():
                form.save()
                messages.success(request, "Employee Information Updated Successfully")
                return redirect("list_employees")
            else:
                messages.error(request, "Employee Update Failed")
                return redirect("edit_employee")
    else:
        raise PermissionDenied("You Are Not An Admin\nPermission Denied")

@login_required
def delete_employee(request, pk):
    if request.user.is_superuser:
        employee = get_object_or_404(Employee, pk=pk)
        # form = EmployeeForm(request.GET or None, instance=employee)
        employee.delete()
        messages.success(request, "Employee Deleted Successfully!")
        return redirect("list_employees")
    else:
        raise PermissionDenied("You Are Not An Admin\nPermission Denied")