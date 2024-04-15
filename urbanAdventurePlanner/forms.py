from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Route, Point


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class RouteForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
    class Meta:
        model = Route
        fields = ['user_id', 'city_id', 'length', 'description']
        widgets = {
            'user_id': forms.HiddenInput(),  # Hide user_id field (assuming it's set in the view)
            'length': forms.HiddenInput(),
            'city_id': forms.HiddenInput()
        }

class PointForm(forms.ModelForm):
    class Meta:
        model = Point
        fields = ['index', 'description', 'address', 'latitude', 'longitude']
        widgets = {
            'latitude': forms.TextInput(attrs={'class': 'form-control'}),
            'longitude': forms.TextInput(attrs={'class': 'form-control'}),                        
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'index': 'Index',
            'description': 'Description',
            'address': 'Address',
            'latitude': 'Latitude',
            'longitude': 'Longitude',
        }

