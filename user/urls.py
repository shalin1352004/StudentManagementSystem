from django.urls import path
from . import views
urlpatterns = [
    path('', views.SignUp, name='signup'),  # URL for the signup page
    path('login/', views.Login, name='login'),  # URL for the login page
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    
]
