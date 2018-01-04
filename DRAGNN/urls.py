from django.urls import path
from . import views

urlpatterns = [
    path('/NeuralNetwork', views.neuralnetwork, name='neuralnet')
]
