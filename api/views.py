from rest_framework.response import Response
from rest_framework.decorators import api_view
from website.models import Customer
from .serializers import CustomerSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['GET'])
def getData(request):
  customers = Customer.objects.all()
  serializer = CustomerSerializer(customers,many=True)
  return Response(serializer.data)