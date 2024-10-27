from django.urls import path
from . import views

urlpatterns = [
    path('',views.clon,name='clone'),
]
