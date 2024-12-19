from django.shortcuts import render, get_object_or_404, redirect
from .models import Guest, Room, Booking, Payment, Service
from .forms import GuestForm, RoomForm, BookingForm, PaymentForm, ServiceForm

# Guest Views
def guest_list(request):
    guests = Guest.objects.all()
    return render(request, 'bookings/guest_list.html', {'guests': guests})

def guest_create(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guest_list')
    else:
        form = GuestForm()
    return render(request, 'bookings/guest_form.html', {'form': form})

def guest_update(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == 'POST':
        form = GuestForm(request.POST, instance=guest)
        if form.is_valid():
            form.save()
            return redirect('guest_list')
    else:
        form = GuestForm(instance=guest)
    return render(request, 'bookings/guest_form.html', {'form': form})

def guest_delete(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == 'POST':
        guest.delete()
        return redirect('guest_list')
    return render(request, 'bookings/guest_confirm_delete.html', {'guest': guest})

# Repeat similar views for Room, Booking, Payment, and Service