from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demoview(request):
    context = {
        'name' : 'john',
        'age' : 50,
        'numbers' : [1,2,3,4],
        'show_numbers' : True,
    }
    return render(request,'templateapp/demoview.html',context)

def home(request):
    return HttpResponse('Home page')