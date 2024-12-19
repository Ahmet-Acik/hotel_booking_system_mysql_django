from django import forms
from .models import Guest, Room, Booking, Payment, Service

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['name', 'email', 'phone', 'address']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_number', 'type', 'price', 'availability']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['guest', 'room', 'check_in_date', 'check_out_date', 'status']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['booking', 'amount', 'payment_date', 'payment_method']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'price']