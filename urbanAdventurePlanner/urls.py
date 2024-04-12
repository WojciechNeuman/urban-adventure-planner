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

]

