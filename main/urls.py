from django.urls import path
from . import views

urlpatterns = [
 path('', views.main, name="main"),
 path('user_appointments/', views.user_appointments, name="user_appointments"),
 path('user_appointments/<int:appointment_id>/', views.show_appointment, name="appointment")
]