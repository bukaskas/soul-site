from .models import Customer, OrderItem
from django.db.models import Q
from datetime import date



def searchCustomers(request):
  search_query = ''
  if request.GET.get("search_query"):
    search_query =request.GET.get('search_query')
    print('SEARCH: ',search_query)
  
  customers = Customer.objects.filter(
    Q(name__icontains=search_query) | Q(phone_nr__icontains=search_query))
  return customers, search_query

def filterService(request):
  search_service_query=''
  if request.GET.get('search_service_query'):
    search_service_query=request.GET.get('search_service_query')
    print('SEARCH: ',search_service_query)
  services = Service.objects.filter(Q(service_name__icontains=search_service_query))
  return services, search_service_query

def beach_use():
  today = date.today()
  bu_total = OrderItem.objects.filter(Q(product__service_name__icontains='day')&Q(created=today))
  return bu_total, today


def sum_payments(*args):
  sum = 0
  for n in args:
    sum += int(0 if n is None else n)
  return sum