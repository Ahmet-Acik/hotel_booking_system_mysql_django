from django.test import TestCase
from .models import Guest, Room, Booking, Payment, Service
from datetime import date

class GuestModelTest(TestCase):
	def test_create_guest(self):
		guest = Guest.objects.create(name="John Doe", email="john@example.com", phone="1234567890", address="123 Main St")
		self.assertEqual(guest.name, "John Doe")
		self.assertEqual(guest.email, "john@example.com")
  
class RoomModelTest(TestCase):
	def test_create_room(self):
		room = Room.objects.create(room_number="101", type="Single", price=100.00, availability=True)
		self.assertEqual(room.room_number, "101")
		self.assertTrue(room.availability)




