from django.urls import path
from . import views

urlpatterns = [
    path("",views.IndexView.as_view(), name="home"),
    path("kitesurfing",views.kitesurfing_view,name="kitesurfing"),
    path("restaurant/",views.RestaurantView.as_view(),name="restaurant"),
    path("restaurant/menu/", views.menu_view, name='menu'),
    path("accommodation",views.AccommodationView.as_view(),name="accommodation"),
    path("thank-you", views.ThankYouView.as_view()),
    # Bookings
    path("bookings",views.BookingsView.as_view(),name="bookings"),
    path("bookings/<int:pk>", views.BookingDetailView.as_view(),name="booking"),
    path("bookings/<str:date>",views.BookingsByDateView.as_view(),name="bookings-by-date"),
    path("book", views.CreateBooking.as_view(), name="book"),
    # Customers pages
    path("signup",views.sign_up_view,name='signup'),
    path("customers",views.customer_index,name='customer-list'),
    path("customer/<str:pk>",views.customer_view,name='customer-view'),
    # services
    path('dayuse/',views.day_use, name="dayuse"),
    path("add-du/",views.add_du, name="add-du"),
    path("add-product/",views.add_product, name="add-product"),
    path("delete-du/<str:pk>",views.delete_dayuse, name="delete-du"),
    path("dayuse-today/",views.today_dayuse, name="today-du"),
    path("customer-cart/<str:pk>",views.customer_cart, name="customer-cart"),
    path("payment/<str:pk>",views.payment, name="payment"),
    path("payments>",views.payment_index, name="payments"),

]

