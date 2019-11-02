from django.urls import path, include
from . import views

urlpatterns= [
    path('', views.home),
    path('home/', views.home),
    path('make/', views.make),
    path('new/', views.new, name='new'),
    path('<room_id>/', views.room),
]