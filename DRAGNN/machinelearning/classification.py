import numpy as np
import math

from DRAGNN.storage import datastore as ds
from DRAGNN.machinelearning import automategeneration as ag
from DRAG.datacontext import context

from sklearn import svm
from sklearn import preprocessing
from sklearn.model_selection import cross_val_predict


def classification():
    time_sig = context["time_signature"]
    ml_data = ds.read_data(time_sig, ds.get_data_store())
    split_data(ml_data)


def split_data(ml_data):
    data = ml_data[0]
    fitness = decompose_fitness(ml_data[1].ravel())

    data = preprocessing.scale(data)
    perform_classification(data, fitness)


def perform_classification(data, fitness):
    clf = svm.SVC(kernel='rbf')
    predictions = cross_val_predict(clf, data, fitness, cv=20)
    print("Predictions: ")
    print(predictions)
    print("\n")
    print("Differences ")
    differences = []
    for predict in range(0, len(predictions)):
        differences.append(predictions[predict] - fitness[predict])
    print(np.asarray(differences))


def log_classification_model(model, testing_data, testing_fitness):
    print("Decision Function: ")
    print(model.decision_function(testing_data))
    print("Mean Accuracy: " + str(model.score(testing_data, testing_fitness)))


def decompose_fitness(fitnesses):
    for fitness in range(len(fitnesses)):
        fitness_val = fitnesses[fitness]
        if fitness_val >= 7:
            fitnesses[fitness] = 2
        elif 4 <= fitness_val < 7:
            fitnesses[fitness] = 1
        else:
            fitnesses[fitness] = 0
    return fitnesses


if __name__ == "__main__":
    classification()
