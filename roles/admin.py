from django.contrib import admin

# Register your models here.
# roles/admin.py

from django.contrib import admin
from .models import Role

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('role_id', 'role_name', 'description', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('role_name',)
