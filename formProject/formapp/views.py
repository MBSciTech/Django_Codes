from django.shortcuts import render,redirect
from .forms import RegistrationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if(form.is_valid()): 
            return redirect('register_success')
    else:
        form = RegistrationForm()
    return render(request,'register.html',{'form':form})

def register_success(request):
    return render(request,'register_success.html')