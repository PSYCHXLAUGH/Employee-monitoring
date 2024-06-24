from django.urls import path
from .views import manager_main_page, manager_profile

urlpatterns = [
    path('', manager_main_page),
    path('profile', manager_profile)
]

