from django.urls import path
from . import views

app_name = 'borame_board'

urlpatterns = [
    path('', views.index, name='index'),
    path('regist/', views.regist, name='regist'),
    path('detail/<int:pk>/',views.detail,name='detail'),
    path('delete/<int:pk>', views.delete, name='delete'),
]

