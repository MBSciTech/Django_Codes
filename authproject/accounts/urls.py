from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signin/',views.signup,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),

]