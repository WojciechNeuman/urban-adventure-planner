from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate


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
    # return render(request, 'registration/password_reset.html')
    return render(request, 'registration/password_reset.html')
    