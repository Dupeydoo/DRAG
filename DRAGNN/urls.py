from django.urls import path

from . import views

"""
Django module containing url routing for the DRAGNN application.
This routing file is always routed through the urls.py routing file
contained in the base DRAG application first.

    Author:
        James

    Version:
        1.0.0
        
    See:
        DRAGNN.views
"""

urlpatterns = [
    path('MachineLearn/', views.machinelearn, name='machinelearning'),
    path('MachineLoad/', views.machineload, name='machineloading'),
    path('Finished/', views.finished, name='finish')
]
"""
urlpatterns (:obj:`list`): contains the controller patterns for different 
typed urls.
"""
