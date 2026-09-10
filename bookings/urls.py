from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_booking, name='add_booking'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('edit/<int:id>/', views.edit_booking, name='edit_booking'),
    path('delete/<int:id>/', views.delete_booking, name='delete_booking'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]