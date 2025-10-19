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

class BookingModelTest(TestCase):
	def setUp(self):
		self.guest = Guest.objects.create(name="Jane Doe", email="jane@example.com")
		self.room = Room.objects.create(room_number="102", type="Double", price=150.00, availability=True)

	def test_create_booking(self):
		booking = Booking.objects.create(
			guest=self.guest,
			room=self.room,
			check_in_date=date(2025, 1, 1),
			check_out_date=date(2025, 1, 5),
			status="Confirmed"
		)
		self.assertEqual(booking.status, "Confirmed")
		self.assertEqual(booking.guest.email, "jane@example.com")



