from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import City, Route, Point


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class InitialRouteForm(forms.ModelForm):
    city_name = forms.ModelChoiceField(queryset=City.objects.all(), label='City Name', widget=forms.Select)
    list_coordinates = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))

    class Meta:
        model = Route
        fields = ['description', 'city_name', 'list_coordinates']
        widgets = {
             'city_name': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 4}),
            'list_coordinates': forms.Textarea(attrs={'rows': 4}),
        }

class RouteForm(forms.ModelForm):
    city_name = forms.CharField()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_id'].required = False
        self.fields['city_id'].required = False
        self.fields['length'].required = False

    class Meta:
        model = Route
        fields = '__all__'  # Include all fields
        
        widgets = {
            'user_id': forms.HiddenInput(),  
            'length': forms.HiddenInput(),
            'city_id': forms.HiddenInput(),
            'description': forms.Textarea(attrs={'rows': 4}),
        }


class PointForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address'].required = False
        self.fields['epsg'].required = False
        self.fields['index'].required = False
        self.fields['route_id'].required = False

    class Meta:
        model = Point
        fields = ['index', 'description', 'address', 'epsg', 'latitude', 'longitude', 'route_id']
        widgets = {
            'latitude': forms.TextInput(attrs={'class': 'form-control'}),
            'longitude': forms.TextInput(attrs={'class': 'form-control'}),                        
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'route_id': forms.HiddenInput(),
        }
        labels = {
            'index': 'Index',
            'description': 'Description',
            'address': 'Address',
            'latitude': 'Latitude',
            'longitude': 'Longitude',
        }