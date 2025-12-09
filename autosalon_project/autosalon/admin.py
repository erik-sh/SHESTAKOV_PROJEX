from django.contrib import admin
from .models import Car, Service, Supplier, TestDriveRequest

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'year', 'price', 'is_sold']
    list_filter = ['brand', 'year', 'is_sold']
    search_fields = ['brand', 'model']
    list_editable = ['is_sold']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'duration']
    search_fields = ['name']

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_person', 'phone', 'rating']
    list_filter = ['rating', 'specialization']

@admin.register(TestDriveRequest)
class TestDriveRequestAdmin(admin.ModelAdmin):
    list_display = ['car', 'name', 'phone', 'preferred_date', 'is_processed']
    list_filter = ['is_processed', 'preferred_date']
    list_editable = ['is_processed']