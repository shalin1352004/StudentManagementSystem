from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_dashboard, name='student_dashboard'),  
    path('add-student/', views.add_student, name='add_student'),# URL for the student dashboard
    path('student/<int:enrollmentNo>/', views.student_detail, name='student_detail'),
 
]