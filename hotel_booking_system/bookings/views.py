from django.shortcuts import render

# Create your views here.
# filepath: /Users/drahmetacik/Projects/hotel_bs_mysql_django/hotel_booking_system/bookings/views.py
from django.shortcuts import render
from .models import Guest, Room, Booking

def guest_list(request):
    guests = Guest.objects.all()
    return render(request, 'bookings/guest_list.html', {'guests': guests})

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'bookings/room_list.html', {'rooms': rooms})

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})