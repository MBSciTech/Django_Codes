from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse('This is home page')
    return render(request,'home.html')

def about(request):
    # return HttpResponse('This is about page')
    return render(request,'about.html')



def contact(request):
    # return HttpResponse('This is contact page')
    return render(request,'contact.html')
