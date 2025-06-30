from django.urls import path
from . import views
urlpatterns = [
    path('', views.result_view, name='result_view'),  # URL for the results view
    path('add_result/', views.add_result, name='add_result'),  
    # URL for adding results
    path('result/<int:rollno>/', views.result_detail, name='result_detail')

    
]
