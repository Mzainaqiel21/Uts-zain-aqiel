
from django.contrib import admin
from django.urls import path
from Kopma_api.views import kopma_list

urlpatterns = [
    path('list/', kopma_list)
]

