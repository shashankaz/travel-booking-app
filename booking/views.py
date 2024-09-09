from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import TravelOption, Booking
from .forms import UserRegisterForm, UserUpdateForm, BookingForm
from .forms import TravelOptionForm

def home(request):
    return render(request, 'booking/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
    return render(request, 'users/profile.html', {'u_form': u_form})

@login_required
def book_travel(request, travel_id):
    travel_option = get_object_or_404(TravelOption, id=travel_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.total_price = travel_option.price * booking.number_of_seats
            booking.save()
            travel_option.available_seats -= booking.number_of_seats
            travel_option.save()
            return redirect('view_bookings')
    else:
        form = BookingForm()
    return render(request, 'booking/book_travel.html', {'form': form, 'travel_option': travel_option})

@login_required
def view_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/view_bookings.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.status = 'Cancelled'
    booking.save()
    return redirect('view_bookings')

@login_required
def list_available_items(request):
    available_travel_options = TravelOption.objects.filter(available_seats__gt=0)
    return render(request, 'booking/available_items.html', {'available_travel_options': available_travel_options})

@login_required
def add_travel_option(request):
    if request.method == 'POST':
        form = TravelOptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_available_items')  
    else:
        form = TravelOptionForm()
    return render(request, 'booking/add_travel_option.html', {'form': form})
