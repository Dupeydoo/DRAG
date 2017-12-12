from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Diversify/', views.diversify, name='diversify'),
    path('RateFitness/', views.fitness, name='fitness')
]
