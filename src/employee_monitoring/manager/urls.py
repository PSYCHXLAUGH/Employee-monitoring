from django.urls import path
from .views import manager_main_page, manager_main_login, manager_main_register
from .views import manager_stats, manager_forms, manager_links, manager_address, reservation

urlpatterns = [
    # mainpage
    path('', manager_main_page),
    path('login', manager_main_login),
    path('register', manager_main_register),
    # profile_panel
    path('statistics', manager_stats),
    path('tables', manager_forms),
    path('address', manager_address),
    path('links', manager_links),
    path('reservation', reservation, name='reservation'),

    # reservation_panel

]

