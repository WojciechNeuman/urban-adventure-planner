from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from urbanAdventurePlanner.models import City, Point
from .forms import InitialRouteForm, RegisterForm, PointForm, RouteForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from .models import Point, Route
import openrouteservice as ors
import ast
import json



# from  django.contrib.auth.decorators import login_required
# @login_required(login_url='/login')
def home(request):
    routes = Route.objects.all()
    return render(request, 'main/home.html', {'routes': routes})

@login_required
def profile(request):
    user = request.user
    routes = Route.objects.filter(user_id=user)
    return render(request, 'main/profile.html', {'routes': routes, 'user': user})

def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user) 

            return redirect('/home')

    else: 
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})

def password_reset(request):
    return render(request, 'registration/password_reset.html')

@login_required
def add_adventure(request):
    if request.method == 'POST':
        form = InitialRouteForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['city_name']
            description = form.cleaned_data['description']
            path = form.cleaned_data['list_coordinates']

            # path = list(path.split("\n"))
            path = ast.literal_eval(path)

            print(path)
            print(type(path))
            print(type(path[0]))

            for i, point in enumerate(path):
                path[i] = [point[1], point[0]]

            client = ors.Client(key='5b3ce3597851110001cf62485835314fc3214662b2893514d1f706b1')

            path_dict = client.directions(
                coordinates=path,
                profile='foot-walking',
                format='geojson',
                options={"avoid_features": ["steps"]},
                validate=False,)
            
            answer = dict()
            answer["distance"] = round(path_dict['features'][0]['properties']['segments'][0]['distance'], 2)
            answer["bbox"] = path_dict['features'][0]['bbox']
            answer["polyline"] = path_dict['features'][0]['geometry']['coordinates']
            answer["points"] = [[path[i][1], path[i][0]] for i in range(len([path]))]
            for i, point in enumerate(answer['polyline']):
                answer['polyline'][i] = (point[1], point[0])

            # answer = json.dumps(answer)
            
            # Get city object based on the provided city_name
            city = City.objects.get(name=city_name)
            
            # Create the Route instance
            route = Route.objects.create(
                length=answer['distance'],  # Set length to -1
                description=description,
                city_id=city,
                user_id=request.user,
                path=json.dumps(answer)
            )

            
            # Redirect to a success page or any other URL
            return redirect('home')  # Change 'success_page' to the appropriate URL name
    else:
        form = InitialRouteForm()
    return render(request, 'main/add_adventure.html', {'form': form})

    
def add_point_form(request):
    if request.method == "POST":
        pass 
    return render(request, 'partials/add_point_form.html', {'point_form': PointForm()})

def display_route(request):
    key = request.GET.get('key')
    route = get_object_or_404(Route, pk=key)
    return render(request, 'main/display_route.html', {'route': route})

def display_routes_in_city(request):
    city_name = request.GET.get('name')
    city = get_object_or_404(City, name=city_name)
    routes = Route.objects.filter(city_id=city.id)
    return render(request, 'main/display_routes_in_city.html', {'routes': routes, 'city': city})

def czechowice_dziedzice(request):
    routes = Route.objects.filter(city_id=1)
    return render(request, 'partials/list_routes.html', {'routes': routes})


def krakow(request):
    route = get_object_or_404(Route, pk=3)
  
    return render(request, 'main/krakow.html')
