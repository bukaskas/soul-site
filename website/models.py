from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


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
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True,blank=True)
    name = models.CharField(max_length=100,null=True)
    phone_nr = models.CharField(max_length=30,null=True)
    email = models.EmailField(blank=True,null=True)
    terms = models.BooleanField(default=False,null=True)
    gender = models.CharField(max_length=8,null=True)
    weight = models.IntegerField(null=True)
    created = models.DateTimeField(editable=False, null=True)
    modified = models.DateTimeField(null=True,blank=True)
    credit = models.IntegerField(null=True,default=0)
    cash_credit = models.IntegerField(null=True, default=0)
   
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
  price = models.IntegerField(null=True,blank=True,editable=False)
  
  @property
  def get_total(self):
    total = self.price*self.quantity
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




class Staff(models.Model):
  UN = 'UN'
  INSTRUCTOR='I'
  ASSISTANT='A'
  B_ASSISTANT='BA'
  RECEPTION='R'
  MANAGER='M'
  HEAD_INSTRUCTOR='HI'

  STAFF_TYPE=[
    (UN, 'Unsigned'),
    (INSTRUCTOR,'Instructor'),
    (ASSISTANT,'Assistant'),
    (B_ASSISTANT,'B-Assistant'),
    (RECEPTION,'Reception'),
    (MANAGER,'Manager'),
    (HEAD_INSTRUCTOR,'Head instructor'),
  ]

  type = models.CharField(max_length=30,choices=STAFF_TYPE,default=UN, null=True,blank=True)
  name = models.CharField(max_length=80)
  phone = models.CharField(max_length=30)
  email = models.CharField(max_length=100)
  user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
  commission = models.IntegerField(null=True,default=0)
   
  def __str__(self):
    return f"{self.name}, phone: {self.phone}"

  def is_instructor(self):
    return self.type in {self.INSTRUCTOR, self.ASSISTANT}
class Session(models.Model):
  service = models.ForeignKey(Service, on_delete=models.SET_NULL,null=True)
  student = models.ManyToManyField(Customer,related_name='students')
  staff = models.ForeignKey(Staff, on_delete=models.SET_NULL,null=True)
  time = models.IntegerField(default=0) 

  def __str__(self):
    return f"Students: {self.student}, Instructor: {self.staff}"
  