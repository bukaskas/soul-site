
# Create your views here.
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.urls import reverse
from .forms import BookingForm, CustomerForm, PaymentForm, CustomUserCreationForm,SessionForm
from django.views.generic.edit import CreateView
from django.http import FileResponse
from .models import *
from datetime import datetime
from django.db.models import Sum
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.decorators.csrf import csrf_exempt
from .utils import searchCustomers, beach_use, sum_payments
from django.core.paginator import Paginator
from django.contrib import messages
from .filters import PaymentFilter
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required



def login_user(request):
    page = 'login'
    if request.user.is_authenticated:
      return redirect('home')

    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        try:
          user = User.objects.get(username=username)
        except:
          messages.add_message(request,messages.ERROR,'User does not exist')
          print('Username does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
          login(request,user)
          return redirect('home')
        else:
          messages.add_message(request,messages.ERROR,'Username or password is incorrect')
    context={
      'page':page
    }
    return render(request,'website//login_register.html',context)
# Create your views here.

def logout_user(request):
    logout(request)
    messages.add_message(request,messages.SUCCESS,'User was succesfully logged out')
    return redirect('login')

def sign_up_view(request):
  form = CustomerForm()
  if request.method == 'POST':
    form = CustomerForm(request.POST)
    if form.is_valid():
      customer = Customer(name=form.cleaned_data['name'],
                          phone_nr=form.cleaned_data['phone_nr'],
                          email=form.cleaned_data['email'],
                          terms=form.cleaned_data['terms'],
                          gender=form.cleaned_data['gender'],
                          weight=form.cleaned_data['weight'],)
      customer.save()
      return redirect('home')
    else:
      form = CustomerForm()

  context = {
    'form':form
  }
  return render(request,'website/customers/sign_up.html',context)

def register_view(request):
  page = 'register'
  form = CustomUserCreationForm()
  if request.method == 'POST':
    print(request.POST)
    form = CustomUserCreationForm(request.POST)
    
    if form.is_valid():
      print("form is valid")
      user = form.save(commit=False)
      user.username = user.username.lower()
      user.save()

      messages.add_message(request,messages.SUCCESS,'User account was created')
      login(request, user)
      return redirect('home')
    else:
      messages.add_message(request, messages.ERROR,"Something went wrong")
 
  context={
    'page':page,
    'form':form,
  }
  return render(request,'website/login_register.html',context)

class IndexView(TemplateView):
  template_name="website/index.html"
 
  def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['service'] = Service.objects.all()
        return context

def kitesurfing_view(request):
  services = Service.objects.all()
  context = {'services':services}

  return render(request,"website/kitesurfing.html",context)

class RestaurantView(View):
  def get(self,request):
    return render(request,"website/restaurant.html")


def menu_view(request):
  menu = open('/Users/audriusbksks/Documents/django/soul/static/pdf/soul_menu.pdf','rb')
  response = FileResponse(menu)
  return response
class AccommodationView(View):
  def get(self,request):
    return render(request,"website/accommodation.html")

 
class CreateBooking(CreateView):
    model=Booking
    form_class = BookingForm
    template_name='website/bookings/book.html'
    success_url="thank-you"

    def form_valid(self,form):
      today = datetime.now()
      return super().form_valid(form)
  

  
class ThankYouView(View):
  def get(self,request):
    return render(request,"soul_customers/thank-you.html")


class BookingsView(ListView):
    template_name = "soul_customers/bookings.html"
    model = Booking
    paginate_by = 10
    ordering = ['-date']
    context_object_name= "bookings"
   
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        bookings = Booking.objects.all()
        date_now = datetime.now()
        all_dates =[i.date for i in bookings if i.date >= date_now.date()]
        def get_unique_numbers(numbers):
          unique = []
          for number in numbers:
            if number not in unique:
                 unique.append(number)
          return unique
        unique_dates = sorted(get_unique_numbers(all_dates))
        sorted_dates = sorted(unique_dates)
        booking_list =[]
        for i in sorted_dates:
          on_date = bookings.filter(date=i.strftime("%Y-%m-%d")).aggregate(Sum('nop'))
          dict ={
            "date":i,
            "num":on_date['nop__sum'],
          }
          booking_list.append(dict)     
        context["booked"]=booking_list
        return context


class BookingDetailView(DetailView):
  template_name = "soul_customers/booking.html"
  model = Booking

  def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        bookings = Booking.objects.all()

class BookingsByDateView(ListView):
    template_name = "soul_customers/bookingsbyday.html"
    model = Booking
    paginate_by = 10
    ordering = ['-date']
    context_object_name= "bookings"


    def get_queryset(self,*args,**kwargs):
      return Booking.objects.filter(date=self.kwargs.get('date'))

    def get_context_data(self, **kwargs):
      context =  super().get_context_data(**kwargs)
      context['booking_date'] = self.kwargs.get('date')
      return context 




def customer_index(request):
  customers, search_query = searchCustomers(request)

  context = {
    'customers':customers,
    'search_query':search_query,
  }
  return render(request,'website/customers/customers-index.html',context)

@login_required(login_url='home')
def customer_view(request,pk):
  customer = Customer.objects.get(id=pk)
  services = Service.objects.all()
  try:
    order = Order.objects.get(customer=customer,complete=False)
  except:
    order = True 
  if request.method == "POST":
    try:
        order = Order.objects.get(customer=customer,complete=False)
    except:
        order = Order(customer=customer)
        order.save()
    product = Service.objects.get(id=request.POST['service-id'])
    order_item = OrderItem(product=product,order=order,quantity=1,price=product.price)
    if customer.credit > 0 and order_item.price == 200:
      order_item.price = 0
      print('DAY USE: ',order_item.price)
    customer.credit += product.credit
    customer.save(update_fields=['credit'])
    order_item.save()
    messages.add_message(request, messages.SUCCESS ,f'Product {product.service_name} was added to the cart.')
    return redirect('customer-view',pk=customer.id)
  
  context = {
    'customer':customer,
    'services':services,
    'order':order,
  }
  return render(request,'website/customers/customer-view.html',context)

# School pages
@login_required(login_url='home')
def day_use(request):
  customers, search_query = searchCustomers(request)
  bu_use, today = beach_use()
  bu = len(bu_use)
  context = {
    'customers':customers,
    'search_query':search_query,
    'total_bu':bu,
    'today':today,
  }
  return render(request, 'website/school/dayuse.html',context)

@login_required(login_url='home')
def add_du(request):
  if request.method == "POST":
    customer_id = request.POST['customer-id']
    customer = Customer.objects.get(id=customer_id)
    try:
        order = Order.objects.get(customer=customer,complete=False)
    except:
        order = Order(customer=customer)
        order.save()
    product = Service.objects.get(service_name__icontains='day')
    order_item = OrderItem(product=product,order=order,quantity=1,price=product.price)
    if customer.credit > 0 and order_item.price == 200:
      order_item.price = 0
      print('DAY USE: ',order_item.price)

    customer.credit += order_item.product.credit
    customer.save(update_fields=['credit'])
    print('Customer credit after: ',customer.credit)
    order_item.save()
  return redirect('dayuse')

def add_session(request):
  """ Add lessons for the instructor and student """
  query_set=''
  query=''
  if request.method == 'GET':
    query_set,query = searchCustomers(request)
    

    
  form = SessionForm()
  try:
    form.fields['student'].queryset = query_set
  except:
    form.fields['student'].queryset = Customer.objects.all()

  context={
    'form':form,
    'query_set':query_set,
    'query':query,

  }
  return render(request,'website/school/add_session.html',context)

@login_required
def add_product(request):
  # create filter to choose service
  products = Service.objects.all()
  product_categories = set([service.category for service in products])
  print("Service types",product_categories)
  # create form for add service
  # need to do drop down to choose service
  context= {
    'services':products,
    'categories':product_categories,
  }
  return render(request, 'website/school/add-service.html',context)


# def customer_index(request):
#   customers = Customer.objects.all()
#   context ={
#     'customer': customers,
#   }
#   return render(request,'website')

@login_required(login_url='home')
def today_dayuse(request):
  day_use, today = beach_use()

  context = {
    'today':today,
    'today_du':day_use,
  }
  return render(request,'website/school/dayuse-today.html',context)

def delete_dayuse(request, pk):
  order_item = OrderItem.objects.get(id=pk)
  if request.method == 'POST':
    order_item.delete()
    order_item.order.customer.credit -= order_item.product.credit
    order_item.order.customer.save(update_fields=['credit'])
    return redirect('customer-view',pk=order_item.order.customer.id)
  context = {
    'object':order_item
  }
  return render(request,'website/delete_template.html',context)

@login_required(login_url='home')
def customer_cart(request, pk):
  order = Order.objects.get(id=pk)
  customer = order.customer

  order_items = order.orderitem_set.all()
  context ={
    'customer':customer,
    'order':order,
    'order_items':order_items,
  }
  return render(request, 'website/school/customer_cart.html',context)

@login_required(login_url='home')
def payment(request, pk):
  form = PaymentForm()
  customer = Customer.objects.get(id=pk)
  order = Order.objects.get(customer=customer,complete=False)
  context = {
    'form':form,
    'customer':customer,
    'order':order,
  }

  if request.method == "POST":
    form = PaymentForm(request.POST)
    if form.is_valid():
      visa=form.cleaned_data['visa']
      cash=form.cleaned_data['cash']
      other=form.cleaned_data['other']
      total = sum_payments(visa,cash,other)

      """Check if the payment amount is equal to carts total"""
      if total == order.get_cart_total:
          payment = Payment(customer = customer,
                      visa=form.cleaned_data['visa'],
                      cash=form.cleaned_data['cash'],
                      other=form.cleaned_data['other'],
                      comment=form.cleaned_data['comment'],
                      order= order)
          payment.save()
          order.complete = True
          """ Return the credits for paid day use """
          order_items = order.orderitem_set.filter(price__gt=0)
          # return count total sum of credit, where credit is equal to 1 
          return_credits = -sum([ item.product.credit for item in order_items if item.product.credit == -1 ])
          # return the credit to the customer
          customer.credit += return_credits
          customer.save(update_fields=['credit'])
          
          order.save(update_fields=['complete'])
          messages.add_message(request, messages.SUCCESS ,f'Payment for {customer.name} was done.')
          return redirect('dayuse')
      else:
        print('Amount was incorrect')
        messages.add_message(request, messages.INFO, f"Customer amount {total} do not match with cart total.")
        form = PaymentForm()
  return render(request, 'website/school/payment.html',context)

@login_required(login_url='home')
def payment_index(request):
  payments = Payment.objects.all()
  my_filter = PaymentFilter(request.GET, queryset=payments)
  payments = my_filter.qs
  cash_payments= payments.filter(cash__isnull=False)
  visa_payments= payments.filter(visa__isnull=False)
  sum_cash = sum([payment.cash for payment in cash_payments])
  sum_visa = sum([payment.visa for payment in visa_payments])
  sum_total = sum_cash + sum_visa
  context = {
    'payments':payments,
    'my_filter':my_filter,
    'total_cash':sum_cash,
    'total_visa':sum_visa,
    'sum_total':sum_total,
  }
  return render(request,'website/school/payment-list.html', context)