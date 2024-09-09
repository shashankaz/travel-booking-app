# Travel Booking Application

## Project Overview

This is a simple Travel Booking web application built using Python and Django. The application allows users to view available travel options, book tickets, and manage their bookings. The frontend is developed using Django templates, with options for styling and responsiveness.

## Features

### User Management
- **Registration**: Users can sign up for an account.
- **Login/Logout**: User authentication is managed using Django's built-in authentication system.
- **Profile Management**: Users can update their profile information.

### Travel Options
- **Travel Options Model**: Allows for the creation of different travel options (Flight, Train, Bus).
- Fields include:
  - Travel Type
  - Source and Destination
  - Date and Time of travel
  - Price
  - Available Seats

### Booking
- **Booking Model**: Users can book travel options by selecting a travel option and the number of seats.
- Each booking stores:
  - User
  - Travel Option
  - Number of Seats
  - Total Price
  - Booking Date
  - Status (Confirmed/Cancelled)
  
### Manage Bookings
- Users can view and manage their current and past bookings.
- Bookings can be canceled if necessary.

### Frontend
- **User Interface**: Simple and user-friendly pages are created using Django templates.
- **Responsiveness**: Pages are designed to be functional across different devices, including desktops and mobile devices.
  
## Technologies Used
- **Django**: Framework for the backend and templating system.
- **SQLite**: To store the data.
- **CSS**: For styling and responsiveness.

## Requirements

- Python 3.x
- Django 3.x or higher

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/shashankaz/travel-booking-app.git
   cd travel-booking-app
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**:
   - The application uses SQLite. No additional configuration is needed for local development.

5. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser** (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the Application**:
   Open a web browser and navigate to `http://127.0.0.1:8000/`.
