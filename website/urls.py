from django.urls import path
from . import views

urlpatterns = [
    path("",views.IndexView.as_view(), name="home"),
    path("kitesurfing",views.kitesurfing_view,name="kitesurfing"),
    path("restaurant",views.RestaurantView.as_view(),name="restaurant"),
    path("accommodation",views.AccommodationView.as_view(),name="accommodation"),
    path("book", views.CreateBooking.as_view(), name="book"),
    path("thank-you", views.ThankYouView.as_view()),
    path("bookings",views.BookingsView.as_view(),name="bookings"),
    path("bookings/<int:pk>", views.BookingDetailView.as_view(),name="booking"),
    path("bookings/<str:date>",views.BookingsByDateView.as_view(),name="bookings-by-date"),
    path("signup",views.sign_up_view,name='signup')
]

