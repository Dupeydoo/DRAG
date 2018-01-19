from django.urls import path, include
from . import views

"""
Django module containing url routing for the DRAGProj application.

    Author:
        James

    Version:
        1.0.0
        
    See:
        DRAJProj.views
"""

urlpatterns = [
    path('', views.index, name='index'),
    path('Diversify/', views.diversify, name='diversify'),
    path('FirstFitness/', views.first_fitness, name='firstfitness'),
    path('RateFitness/', views.fitness, name='fitness'),
    path('DRAGError/', views.error, name='error'),
    path('Preset/', views.preset, name='preset')
]
"""
urlpatterns (:obj:`list`): contains the controller patterns for different typed urls.
"""
