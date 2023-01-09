from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

# Create your views here.

def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def admin(request):
    return render(request, 'admin.html')

def welcome_user(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
    'user' : User.objects.get(id=request.session['user_id']), 
    }
    return render(request, 'welcome_user.html', context)

def register(request):
    errors = User.objects.user_validator(request.POST)
    if len(errors) > 0: 
        for msg in errors.values():
            messages.error(request, msg)
        return redirect('/')
    password = request.POST['password']
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    user = User.objects.create(
        first_name = request.POST['fname'].title(),
        last_name = request.POST['lname'],
        email = request.POST['email'],
        password = hashed,
    )
    request.session['user_id'] = user.id
    return redirect('/welcome_user')

def login(request):
    errors = User.objects.registration_validator(request.POST)
    if len(errors) > 0:
        for msg in errors.values():
            messages.error(request, msg)  
    user_login_email = User.objects.filter(email=request.POST['email'])
    if len(user_login_email) > 0:
        first_user = user_login_email[0]
        if bcrypt.checkpw(request.POST['password'].encode(), first_user.password.encode()):
            request.session['user_id'] = first_user.id
            return redirect('/welcome_user')
    messages.error(request, "Email/Password Invalid!")
    return redirect('/admin_login')

def logout(request):
    del request.session['user_id']
    return redirect('/')