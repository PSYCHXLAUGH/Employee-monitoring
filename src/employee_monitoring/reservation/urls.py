from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='reservation_main'), #  /reservation/ main page
    path('<int:table_id>/', views.table_list),  # /reservation/<slug>
]
