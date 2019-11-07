from django.urls import path, include
from . import views

urlpatterns= [
    path('make/', views.make),
    path('enter/', views.enter),
    path('room/', views.room),
    path('<encrypt>/', views.room),
    path('list/<uid>/', views.list),
    path('memo/<encrypt>/', views.memo),
    path('delete/<uid>/<encrypt>/', views.delete),
]