from .forms import BookingForm
from django.test import TestCase

from django.test import TestCase
from .models import Guest, Room, Booking, Payment, Service
from datetime import date
from decimal import Decimal
from django.urls import reverse

class GuestModelTest(TestCase):
	def test_create_guest(self):
		guest = Guest.objects.create(name="John Doe", email="john@example.com", phone="1234567890", address="123 Main St")
		self.assertEqual(guest.name, "John Doe")
		self.assertEqual(guest.email, "john@example.com")

	def test_invalid_email(self):
		guest = Guest(name="Invalid Email", email="not-an-email")
		with self.assertRaises(Exception):
			guest.full_clean()
  
class RoomModelTest(TestCase):
	def test_create_room(self):
		room = Room.objects.create(room_number="101", type="Single", price=100.00, availability=True)
		self.assertEqual(room.room_number, "101")
		self.assertTrue(room.availability)

	def test_update_room(self):
		from decimal import Decimal
		room = Room.objects.create(room_number="201", type="Double", price=Decimal('120.00'), availability=True)
		room.price = Decimal('130.00')
		room.save()
		updated_room = Room.objects.get(room_number="201")
		self.assertEqual(updated_room.price, Decimal('130.00'))

	def test_delete_room(self):
		room = Room.objects.create(room_number="301", type="Suite", price=Decimal('200.00'), availability=True)
		room_id = room.id
		room.delete()
		self.assertFalse(Room.objects.filter(id=room_id).exists())
class BookingPaymentCascadeTest(TestCase):
	def setUp(self):
		from decimal import Decimal
		self.guest = Guest.objects.create(name="Cascade Guest", email="cascade@example.com")
		self.room = Room.objects.create(room_number="401", type="Suite", price=Decimal('300.00'), availability=True)
		self.booking = Booking.objects.create(
			guest=self.guest,
			room=self.room,
			check_in_date=date(2025, 3, 1),
			check_out_date=date(2025, 3, 5),
			status="Confirmed"
		)
		self.payment = Payment.objects.create(
			booking=self.booking,
			amount=Decimal('1200.00'),
			payment_date=date(2025, 3, 1),
			payment_method="Credit Card"
		)

	def test_delete_booking_cascades_payment(self):
		self.booking.delete()
		self.assertFalse(Payment.objects.filter(id=self.payment.id).exists())

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

class PaymentModelTest(TestCase):
	def setUp(self):
		self.guest = Guest.objects.create(name="Alice", email="alice@example.com")
		self.room = Room.objects.create(room_number="103", type="Suite", price=200.00, availability=True)
		self.booking = Booking.objects.create(
			guest=self.guest,
			room=self.room,
			check_in_date=date(2025, 2, 1),
			check_out_date=date(2025, 2, 3),
			status="Paid"
		)

	def test_create_payment(self):
		payment = Payment.objects.create(
			booking=self.booking,
			amount=400.00,
			payment_date=date(2025, 2, 1),
			payment_method="Credit Card"
		)
		self.assertEqual(payment.amount, 400.00)
		self.assertEqual(payment.payment_method, "Credit Card")

class ServiceModelTest(TestCase):
	def test_create_service(self):
		service = Service.objects.create(name="Breakfast", description="Buffet breakfast", price=20.00)
		self.assertEqual(service.name, "Breakfast")
		self.assertEqual(service.price, 20.00)



class GuestListViewTest(TestCase):
	def setUp(self):
		Guest.objects.create(name="Test Guest", email="testguest@example.com")

	def test_guest_list_view_status_code_and_template(self):
		url = reverse('guest_list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'bookings/guest_list.html')

class BookingFormTest(TestCase):
	def setUp(self):
		from decimal import Decimal
		self.guest = Guest.objects.create(name="Form Guest", email="formguest@example.com")
		self.room = Room.objects.create(room_number="501", type="Single", price=Decimal('100.00'), availability=True)

	def test_booking_form_valid(self):
		data = {
			'guest': self.guest.id,
			'room': self.room.id,
			'check_in_date': '2025-04-01',
			'check_out_date': '2025-04-05',
			'status': 'Confirmed'
		}
		form = BookingForm(data)
		self.assertTrue(form.is_valid())
		booking = form.save()
		self.assertEqual(booking.status, 'Confirmed')

