from django.urls import path
from .views import signup,login_view,verify,logout_view



urlpatterns = [
    path('',signup,name='signup'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('verify/<str:token>/',verify,name='verification')
]