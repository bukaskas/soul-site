from django.contrib import admin
from .models import Customer, Booking, Service
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
  list_display=("name","phone_nr")

class ServiceAdmin(admin.ModelAdmin):
  list_display=("service_name","price")


admin.site.register(Service,ServiceAdmin)
admin.site.register(Customer,CustomerAdmin)

