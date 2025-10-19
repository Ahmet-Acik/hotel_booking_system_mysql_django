from django.test import TestCase
from .models import Guest, Room, Booking, Payment, Service
from datetime import date

class GuestModelTest(TestCase):
	def test_create_guest(self):
		guest = Guest.objects.create(name="John Doe", email="john@example.com", phone="1234567890", address="123 Main St")
		self.assertEqual(guest.name, "John Doe")
		self.assertEqual(guest.email, "john@example.com")



