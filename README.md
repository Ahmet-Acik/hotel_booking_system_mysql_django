
# Hotel Booking System

This is a Django-based hotel booking system that allows users to manage guests, rooms, bookings, payments, and services. The system provides a web interface for administrators to perform CRUD operations on these entities.

## Features

- Manage Guests: Add, update, delete, and list guests.
- Manage Rooms: Add, update, delete, and list rooms.
- Manage Bookings: Add, update, delete, and list bookings.
- Manage Payments: Add, update, delete, and list payments.
- Manage Services: Add, update, delete, and list services.
- Customizable Admin Interface: Custom admin site with personalized titles.

## Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/Ahmet-Acik/hotel_bs_mysql_django.git
   cd hotel_bs_mysql_django
   ```

2. **Create a Virtual Environment**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```sh
   pip install -r hotel_booking_system/requirements.txt
   ```

4. **Apply Migrations**:
   ```sh
   python hotel_booking_system/manage.py makemigrations
   python hotel_booking_system/manage.py migrate
   ```

5. **Create a Superuser**:
   ```sh
   python hotel_booking_system/manage.py createsuperuser
   ```

6. **Run the Development Server**:
   ```sh
   python hotel_booking_system/manage.py runserver
   ```

## Usage
### Run Tests

To run tests for the bookings app, use:

```sh
python hotel_booking_system/manage.py test bookings
```

### Access the Admin Interface

1. Open your web browser and go to `http://127.0.0.1:8000/admin/`.
2. Log in with the superuser credentials you created.

### Manage Guests

- **List Guests**: View a list of all guests.
- **Add Guest**: Add a new guest.
- **Update Guest**: Edit an existing guest.
- **Delete Guest**: Delete a guest.

### Manage Rooms

- **List Rooms**: View a list of all rooms.
- **Add Room**: Add a new room.
- **Update Room**: Edit an existing room.
- **Delete Room**: Delete a room.

### Manage Bookings

- **List Bookings**: View a list of all bookings.
- **Add Booking**: Add a new booking.
- **Update Booking**: Edit an existing booking.
- **Delete Booking**: Delete a booking.

### Manage Payments

- **List Payments**: View a list of all payments.
- **Add Payment**: Add a new payment.
- **Update Payment**: Edit an existing payment.
- **Delete Payment**: Delete a payment.

### Manage Services

- **List Services**: View a list of all services.
- **Add Service**: Add a new service.
- **Update Service**: Edit an existing service.
- **Delete Service**: Delete a service.

## Custom Admin Site

The admin site has been customized with personalized titles. You can further customize it by editing the `admin_site.py` file.

## Project Structure

```
hotel_booking_system/
    bookings/
        __init__.py
        admin.py
        apps.py
        forms.py
        models.py
        views.py
        urls.py
        templates/
            bookings/
                booking_form.html
                guest_form.html
                room_form.html
                booking_confirm_delete.html
                guest_confirm_delete.html
                room_confirm_delete.html
                booking_list.html
                guest_list.html
                room_list.html
    hotel_booking_system/
        __init__.py
        settings.py
        urls.py
        wsgi.py
        admin_site.py
    manage.py
    requirements.txt
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For any questions or suggestions, please contact [a.acik@icloud.com].

