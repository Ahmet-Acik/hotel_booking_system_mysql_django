# filepath: /Users/drahmetacik/Projects/hotel_bs_mysql_django/hotel_booking_system/bookings/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('guests/', views.guest_list, name='guest_list'),
    path('rooms/', views.room_list, name='room_list'),
    path('bookings/', views.booking_list, name='booking_list'),
]