from django.urls import path
from . import views
from django.views.generic.base import TemplateView



urlpatterns = [
    path('upload/',views.upload,name='upload'),
    path('signup/',views.signup,name='signup'),
    path('',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('index/',views.index,name='index'),
    path('logout/',views.logout,name='logout'),
]