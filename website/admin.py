from django.contrib import admin
from .models import Customer, Service, Order, OrderItem, Payment
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

admin.site.register(Service,ServiceAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)
admin.site.register(Payment,PaymentAdmin)

