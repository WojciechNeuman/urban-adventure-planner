from django.shortcuts import get_object_or_404, render, redirect

from urbanAdventurePlanner.models import City, Point
from .forms import RegisterForm, PointForm, RouteForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from .models import Point, Route



# from  django.contrib.auth.decorators import login_required
# @login_required(login_url='/login')
def home(request):
    return render(request, 'main/home.html')

def profile(request):
    return render(request, 'main/profile.html')

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


# def add_adventure(request):
#     context = {'route_form': RouteForm(), 'point_form': PointForm()}
#     return render(request, 'main/add_adventure.html', context=context)

@login_required
def add_adventure(request):
    print("W FUNKCJI")
    if request.method == 'POST':
        print("POST")
        form = RouteForm(request.POST)
        if form.is_valid():
            route = form.save(commit=False)
            route.user_id = request.user
            route.city_id = 1  # Assuming city_id is static
            route.length = -1   # Assuming length is static
            route.save()
            return redirect(request.path)
            # return redirect('')  # Redirect to home page after successful submission
    else:
        print("ELSE")
        form = RouteForm()
    return render(request, 'main/add_adventure.html', {'route_form': form})

# @login_required
# def add_adventure(request):
#     print("W FUNKCJI")

#     # PointFormSet = modelformset_factory(Point, form=PointForm, extra=0)
#     # point_formset = formset_factory(PointForm, absolute_max=1500)
#     PointFormSet = formset_factory(PointForm, extra=0, absolute_max=100, max_num=100)
#     data = {
#      "form-TOTAL_FORMS": "100",
#      "form-INITIAL_FORMS": "0",
#     }
#     point_formset = PointFormSet(request.POST, prefix='point')
#     point_formset
#     print(point_formset.errors)

#     print(f'YYY{point_formset.is_valid()}')

#     if request.method == 'POST':
#         route_form = RouteForm(request.POST)

#         if route_form.is_valid():
#             route = route_form.save(commit=False)
#             route.user_id = request.user
#             route.city_id = City.objects.get(pk=1)  # Assuming city_id is static
#             route.length = -1  # Assuming length is static
#             # route.save()

#             print(f'point_formset: {point_formset}')
#             pass
#             if point_formset.is_valid():
#                 instances = point_formset.save(commit=False)
#                 for instance in instances:
#                     instance.route_id = route
#                     instance.save()
#         else:
#             point_formset = point_formset(request.POST, prefix='point')
#     else:
#         print("XXXX NIE POST")
#         route_form = RouteForm()
#         point_formset = point_formset(queryset=Point.objects.none(), prefix='point')

#     return render(request, 'main/add_adventure.html', {'route_form': route_form, 'point_formset': point_formset})

    
def add_point_form(request):
    if request.method == "POST":
        pass 
    return render(request, 'partials/add_point_form.html', {'point_form': PointForm()})

def czechowice_dziedzice(request):
    route = get_object_or_404(Route, pk=3)
    return render(request, 'main/czechowice_dziedzice.html', {'route': route})


def krakow(request):
    route = get_object_or_404(Route, pk=3)

    return render(request, 'main/krakow.html')


# @login_required
# def add_adventure(request):
#     PointFormSet = modelformset_factory(Point, form=PointForm, extra=0)

#     if request.method == 'POST':
#         route_form = RouteForm(request.POST)

#         if route_form.is_valid() and point_formset.is_valid():
#             route = route_form.save(commit=False)
#             route.user_id = request.user
#             route.city_id = City.objects.get(pk=1)  # Assuming city_id is static
#             route.length = -1  # Assuming length is static
#             route.save()

#              # extract every point-form from route_form and with id point-form and save them with point.route_id = route
#     else:
#         route_form = RouteForm()
#         point_formset = PointFormSet(queryset=Point.objects.none())

#     return render(request, 'main/add_adventure.html', {'route_form': route_form, 'point_formset': point_formset})