
# Create your views here.
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.urls import reverse
from .forms import BookingForm, CustomerForm
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from .models import Service,Customer,Booking
from datetime import datetime
from django.db.models import Sum
from django.views.generic.list import ListView
from django.views.generic import DetailView




# Create your views here.
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

class AccommodationView(View):
  def get(self,request):
    return render(request,"website/accommodation.html")

 
class CreateBooking(CreateView):
    model=Booking
    form_class = BookingForm
    template_name='soul_customers/book.html'
    success_url="thank-you"

    def form_valid(self,form):

      # date_clean = date.fromisoformat(date_form)
      today = datetime.now()
      today_string = today.strftime("%Y-%m-%d")
      print("---- BOOKING DATE ----")

      print("STRING:",today_string)
      print("---- BOOKING DATE ----")
      return super().form_valid(form)
  


# class SignUpView(CreateView):
#     model = Customer
#     fields = "__all__"
#     template_name ="soul_customers/signup.html"
#     success_url = "thank-you"

  
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
        # Add in a QuerySet of all the books

        # Need to remove after the date passed

        # last_booking = Booking.objects.last()
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
      print("_________")

      print(context['booking_date'])

      print("_________")

      return context 

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
  return render(request,'soul_customers/sign_up.html',context)