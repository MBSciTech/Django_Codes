from django.urls import path
from . import views

urlpatterns = [
    path('',views.demoview , name='demoview'),
]