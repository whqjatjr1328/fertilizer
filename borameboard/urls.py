from django.urls import path
from . import views

app_name = 'borame_board'

urlpatterns = [
    path('', views.index, name='index'),
]

