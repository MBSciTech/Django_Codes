# Place templates in 'accounts/templates/' directory as per Django app convention
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'POST':  # Fixed typo here
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,'Signup successful, Welcome')
            return redirect('home')
    else:
        form= UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    # messages.success(request, 'Logged out successfully!')
    # return redirect('login')
    return render(request,'logout.html')


