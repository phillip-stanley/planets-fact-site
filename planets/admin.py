from django.contrib import admin
from .models import Planet


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'updated_at', 'status']
    list_filter = ['status', 'created_at', 'updated_at']
    search_fields = ['name', 'overview']
    prepopulated_fields = {'slug': ['name']}
    date_hierarchy = 'created_at'
    ordering = ['created_at', 'updated_at']
