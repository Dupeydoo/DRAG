from django.urls import path
from . import views

urlpatterns = [
    path('MachineLearn/', views.machinelearn, name='machinelearning'),
    path('Finished/', views.finished, name='finish')
]
