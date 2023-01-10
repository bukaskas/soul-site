import django_filters
from django_filters import *
from .models import *




class PaymentFilter(django_filters.FilterSet):
  customer = django_filters.CharFilter(field_name='customer__name',lookup_expr='icontains')
  cash = django_filters.BooleanFilter(field_name='visa',lookup_expr='isnull')
  start_date = django_filters.DateFilter(field_name='created', lookup_expr='gte')
  end_date = django_filters.DateFilter(field_name='created',lookup_expr='lte')
  class Meta:
    model = Payment
    fields = {'customer','cash','created'}
    exclude=[]
  
    
