from django.contrib import admin
from django.urls import path,include
from myapp.views import ToDoAPI,ToDosAPI

urlpatterns = [
    path('<int:pk>/', ToDoAPI.as_view()),
    path('', ToDosAPI.as_view()),
]
