from django.contrib import admin
from django.urls import path,include
from myapp.views import ToDo,ToDosAPI

urlpatterns = [
    path('', ToDosAPI.as_view()),
]
