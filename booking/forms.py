from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Booking
from .models import TravelOption

# User Registration Form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# User Update Form
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

# Booking Form
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['travel_option', 'number_of_seats']

    def clean(self):
        cleaned_data = super().clean()
        travel_option = cleaned_data.get('travel_option')
        number_of_seats = cleaned_data.get('number_of_seats')
        if travel_option and number_of_seats > travel_option.available_seats:
            raise forms.ValidationError('Not enough seats available')

class TravelOptionForm(forms.ModelForm):
    class Meta:
        model = TravelOption
        fields = ['travel_type', 'source', 'destination', 'date_time', 'price', 'available_seats']