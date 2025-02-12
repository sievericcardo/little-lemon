from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Booking


# Code added for loading form data on the Booking page
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
