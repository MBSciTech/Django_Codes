from django.urls import path
from . import views

urlpatterns = [
    path('demoview/',views.demoview , name='demoview'),
    path('',views.home,name='home'),

]