from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    # path('login', views.login, name='login'),
    path('sign-up', views.sign_up, name='sign-up'),
    path('profile', views.profile, name='profile-page'),
    path('password_reset', views.password_reset, name='password_reset'),
    path('add-adventure', views.add_adventure, name='add-adventure'),
    path('add-adventure/add-point', views.add_point_form, name='add-point'), # URL path / view in use / link in {% %}
    path('czechowice-dziedzice', views.czechowice_dziedzice, name='czechowice-dziedzice'),
    path('display_routes_in_city', views.display_routes_in_city, name='display_routes_in_city'),
    path('display_route', views.display_route, name='display_route'),
    path('krakow', views.krakow, name='krakow'),
]