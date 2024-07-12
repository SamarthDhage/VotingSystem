from django.contrib import admin
from django.urls import path
from . import views


app_name = 'parties'

urlpatterns = [
    path('create/', views.create_party, name='party_form'),  # Use views.create_party here
]


