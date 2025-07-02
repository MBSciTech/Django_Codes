from django.urls import path
from . import views

urlpatterns = [
    path('demoview/',views.demoview , name='demoview')
]