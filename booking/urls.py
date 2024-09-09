from django.urls import path
from . import views

urlpatterns = [
    # Home and other URLs
    path('', views.home, name='home'),

    # User Management
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),

    # Travel Booking URLs
    path('book/<int:travel_id>/', views.book_travel, name='book_travel'),
    
    # Manage Bookings
    path('my-bookings/', views.view_bookings, name='view_bookings'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),

    # Available Items for Booking
    path('available-items/', views.list_available_items, name='list_available_items'),

    # Add New Travel Option
    path('add-travel-option/', views.add_travel_option, name='add_travel_option'),
]
