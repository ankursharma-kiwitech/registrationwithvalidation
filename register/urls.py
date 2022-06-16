
from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.RegistrationAPIView, name='register'),
    path('address',views.UserAddressesAPIView),
    path('details', views.ListUserAPIView, name='details'),
]
