
from app.views import index,Signup,Login,logout,events,you_invited

from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

# from users import views as user_views


urlpatterns = [
    path('',index,name='homepage'),
    path('signup/',Signup.as_view(),name='signup'),
    path('login/',Login.as_view(),name='login'),
    path('logout/',logout,name='logout'),
    path('add/',events.add_an_event,name='add_event'),
    path('see_you_invited/',you_invited.you_invited,name='you_invited')
   

   
]