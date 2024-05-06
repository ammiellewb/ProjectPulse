from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import User

# Create your views here.
def login(request):
    if request.method == "POST":
        email = request.POST.get('email', "")
        password = request.POST.get('password', "")
        print(email, password)

        if email and password:
            print("Auth the user")
            user = authenticate(request, email=email, password=password)
            if user is not None:
                print("Log in the user")
                auth_login(request, user)
                return redirect("/projects/")

    return render(request, 'account/login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username', "")
        email = request.POST.get('email', "")
        password1 = request.POST.get('password1', "")
        password2 = request.POST.get('password2', "")

        if username and email and password1 and password2:
            print("Create the user")
            user = User.objects.create_user(username, email, password1)
            return redirect("/login/")
        else:
            print("All fields are required")
    else:
        print("Just show the form")
    return render(request, 'account/signup.html')

def logout(request):
    auth_logout(request)
    return redirect("/")