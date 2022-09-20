from django.urls import path
from . import views



urlpatterns = [
    path('profile/',views.profile,name='profile'),
    path('upload/',views.upload,name='upload'),
    path('signup/',views.signup,name='signup'),
    path('',views.login, name='login'),
    path('home/',views.home,name='home'),
    
]