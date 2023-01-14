from django.contrib import admin
from .models import *
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
  list_display=("name","phone_nr")

class ServiceAdmin(admin.ModelAdmin):
  list_display=("service_name","price")

class OrderAdmin(admin.ModelAdmin):
  list_display = ['customer']

class OrderItemAdmin(admin.ModelAdmin):
  list_display = ['product','order','quantity','created']

class PaymentAdmin(admin.ModelAdmin):
  list_display=['created','customer','visa','cash','other','comment']

class StaffAdmin(admin.ModelAdmin):
  list_display = ['type','name','phone','email','user']

class SessionAdmin(admin.ModelAdmin):
  list_display = ['service','staff','time','get_students']
  
  def get_students(self, obj):
        return [student.name for student in obj.student.all()]


admin.site.register(Service,ServiceAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)
admin.site.register(Payment,PaymentAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Session, SessionAdmin)


