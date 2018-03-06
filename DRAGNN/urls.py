from django.urls import path
from . import views

urlpatterns = [
    path('MachineLearn/', views.machinelearn, name='machinelearning'),
    path('MachineLoad/', views.machineload, name='machineloading'),
    path('Finished/', views.finished, name='finish')
]
