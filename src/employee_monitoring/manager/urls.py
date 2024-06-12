from django.urls import path
from .views import manager_main_page

urlpatterns = [
    path('', manager_main_page)
]
