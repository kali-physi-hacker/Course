from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from course.models.category import Category
from course.forms.category import CategoryForm


@login_required
def list_categories(request):
    template = "category/list.html"
    categories = Category.objects.all()
    context = {"categories": categories, "list_category_active": "active", "category_show": "show",
            "category_active": "active"}
    return render(request, template, context)


@login_required
def add_category(request):
    template = "category/add.html"
    form = CategoryForm()
    context = {"form": form, "add_category_active": "active", "category_show": "show", "category_active": "active"}
    return render(request, template, context)


@login_required
def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Category Created Successfully")
            return redirect("list_categories")
        else:
            messages.error(request, "Category Creation Failed!")
            return redirect("add_category")


@login_required
def edit_category(request, pk):
    if request.user.is_superuser:
        template = "category/edit.html"
        category = get_object_or_404(Category, pk=pk)
        form = CategoryForm(request.GET or None, instance=category)
        context = {"form": form, "pk": pk}
        return render(request, template, context)
    else:
        raise PermissionDenied(" ")



@login_required
def update_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST or None, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Category Update Successfully")
            return redirect("list_categories")
        else:
            raise PermissionDenied("You Are Not An Admin\nPermission Denied")


@login_required
def delete_category(request, pk):
    if request.user.is_superuser:
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        messages.success(request, "Rank Deleted Successfully")
        return redirect("list_categories")
    else:
        raise PermissionDenied("You Are Not An Admin\nPermission Denied")