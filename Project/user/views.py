from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import User

# Dashboard view
def dashboard(request):
    return render(request, 'user/dashboard.html')

# User login view
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def user_login(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')

        # Try to find the user by username or email
        try:
            user = User.objects.get(username=username_or_email)  # Try username first
        except User.DoesNotExist:
            try:
                user = User.objects.get(email=username_or_email)  # Try email if username doesn't exist
            except User.DoesNotExist:
                user = None

        # Check if the user was found and if the password matches
        if user and user.password == password:  # Compare plain text passwords
            request.session['user_id'] = user.id  # Manually create session
            return redirect('dashboard')  # Redirect to the dashboard
        else:
            messages.error(request, 'Invalid username or email, or password.')

    return render(request, 'user/login.html')

# User registration view
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Save the user without hashing the password
        user = User(
            name=name,
            email=email,
            username=username,
            password=password  # Save the password as plain text (no hashing)
        )
        user.save()

        return redirect('login')  # Redirect to login page
    return render(request, 'user/register.html')

