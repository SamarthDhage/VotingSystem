from django.contrib import admin
from django.urls import path
from .views import home,vote,results

urlpatterns = [
    path("", home, name="home"),
    path('vote/',vote,name = 'vote' ),
    path('results/', results, name='results'),
]
