from django.shortcuts import render

# Create your views here.
# roles/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Role
from .forms import RoleForm
from django.contrib import messages

def role_list(request):
    roles = Role.objects.filter(status=True)
    return render(request, 'roles/role_list.html', {'roles': roles})

def create_role(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Role created successfully!')
            return redirect('role_list')
    else:
        form = RoleForm()
    return render(request, 'roles/create_role.html', {'form': form})

def update_role(request, pk):
    role = get_object_or_404(Role, pk=pk)
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            messages.success(request, 'Role updated successfully!')
            return redirect('role_list')
    else:
        form = RoleForm(instance=role)
    return render(request, 'roles/update_role.html', {'form': form})

def delete_role(request, pk):
    role = get_object_or_404(Role, pk=pk)
    role.status = False
    role.save()
    messages.warning(request, 'Role has been deactivated (soft deleted).')
    return redirect('role_list')
