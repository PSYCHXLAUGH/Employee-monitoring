from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation_mainpage, name='reservation_mainpage'),  # / main page
    path('<int:table_id>/', views.reservation_table, name='reservation_table'),  # /<table_id>
    path('<int:table_id>/', views.reservation_table, name='reservation_table'),  # /<table_id>
]
