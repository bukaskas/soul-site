from django.db import models
from django.utils import timezone

# Create your models here.

class Service(models.Model):
    service_name = models.CharField(max_length=20)
    price = models.IntegerField()
    time = models.FloatField(null=True)
    category = models.CharField(null=True,max_length=40) #in category [kitesurfing, yoga, fitness, event]
    image = models.ImageField(null=True, blank=True)
    credit = models.IntegerField(null=True,blank=True)


    def __str__(self):
      return f" {self.service_name}, {self.price}"

class Customer(models.Model):
    name = models.CharField(max_length=100,null=True)
    phone_nr = models.CharField(max_length=30,null=True)
    email = models.EmailField(blank=True,null=True)
    terms = models.BooleanField(default=False,null=True)
    gender = models.CharField(max_length=8,null=True)
    weight = models.IntegerField(null=True)
    created = models.DateTimeField(editable=False, null=True)
    modified = models.DateTimeField(null=True,blank=True)
    credit = models.IntegerField(null=True,default=0)

    # many bookings
    def __str__(self):
      return f"{self.name},{self.phone_nr}"
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Customer, self).save(*args, **kwargs)


class Booking(models.Model):
    date = models.DateField(verbose_name="Booking date")
    customer_name = models.CharField(max_length=100)
    customer_fname = models.CharField(max_length=100,null=True)
    contact_number= models.CharField(max_length=30,null=True)
    nop = models.IntegerField(null=True)
    service = models.ForeignKey(Service,on_delete=models.SET_NULL, null=True,related_name="service")

    @property
    def customer_full_name(self):
       return f"{self.customer_name} {self.customer_fname}"

    def __str__(self):
      return f"{self.date}, {self.service}, {self.nop} "




class Order(models.Model):
  complete = models.BooleanField(default=False)
  customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
  complete = models.BooleanField(null=True, default=False)

  def __str__(self):
    return str(self.id)

  @property
  def get_cart_total(self):
    orderitems = self.orderitem_set.all()
    total = sum([item.get_total for item in orderitems])
    return total
  
  @property
  def get_order_items(self):
    orderitems = self.orderitem_set.all()
    total_items = sum([item.quantity for item in orderitems])
    return total_items

  def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Order, self).save(*args, **kwargs)

class OrderItem(models.Model):
  product = models.ForeignKey(Service,on_delete=models.SET_NULL,null=True)
  order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
  quantity = models.IntegerField(default=0, null=True,blank=True)
  created = models.DateField(null=True,editable=False)
  modified = models.DateField(null=True,editable=False)
  
  @property
  def get_total(self):
    total = self.product.price*self.quantity
    return total

  def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(OrderItem, self).save(*args, **kwargs)
  def __str__(self):
    return f'{self.product}, {self.quantity}'

  # create payment model
class Payment(models.Model):
  customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
  visa = models.IntegerField(null=True,blank=True)
  cash = models.IntegerField(null=True,blank=True)
  other = models.IntegerField(null=True,blank=True)
  comment = models.TextField(max_length=100,blank=True)
  created = models.DateField(null=True,editable=False)
  modified = models.DateField(null=True,editable=False)
  order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)

  

  def save(self, *args, **kwargs):
          ''' On save, update timestamps '''
          if not self.id:
              self.created = timezone.now()
          self.modified = timezone.now()
          return super(Payment, self).save(*args, **kwargs)
  def __str__(self):
      return f'{self.customer}, Visa: {self.visa} Cash:{self.cash}'

