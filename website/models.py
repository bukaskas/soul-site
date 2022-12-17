from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100,null=True)
    phone_nr = models.CharField(max_length=30,null=True)
    email = models.EmailField(blank=True,null=True)
    terms = models.BooleanField(default=False,null=True)
    gender = models.CharField(max_length=8,null=True)
    weight = models.IntegerField(null=True)


    # many bookings
    def __str__(self):
      return f"{self.name},{self.phone_nr}"

class Service(models.Model):
    service_name = models.CharField(max_length=20)
    price = models.IntegerField()
    time = models.FloatField(null=True)
    category = models.CharField(null=True,max_length=40) #in category [kitesurfing, yoga, fitness, event]
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
      return f" {self.service_name}, {self.price}"


class Booking(models.Model):
    date = models.DateField(verbose_name="Booking date")
    customer_name = models.CharField(max_length=100)
    customer_fname = models.CharField(max_length=100)
  #  nop = number of people
    contact_number= models.CharField(max_length=30,null=True)
    nop = models.IntegerField()
    service = models.ForeignKey(Service,on_delete=models.SET_NULL, null=True,related_name="booking")
    def customer_full_name(self):
     
       return f"{self.customer_name} {self.customer_fname}"
    # one service
    # one customer
    # add method to calculate of total bookings on this date

    def __str__(self):
      return f"{self.date}, {self.service}, {self.nop} "


