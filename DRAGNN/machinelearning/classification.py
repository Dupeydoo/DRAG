import numpy as np
import math

from DRAGNN.storage import datastore as ds
from DRAGNN.machinelearning import automategeneration as ag
from DRAG.datacontext import context

from sklearn import svm
from sklearn import preprocessing
from sklearn.model_selection import cross_val_predict
from sklearn import tree
import uuid


def classification():
    time_sig = context["time_signature"]
    ml_data = ds.read_data(time_sig, ds.get_data_store())
    split_data(ml_data)


def split_data(ml_data):
    data = ml_data[0]
    features = len(data[0])
    # data = preprocessing.scale(data)
    fitness = decompose_fitness(ml_data[1].ravel())

    enc = preprocessing.OneHotEncoder()
    data = enc.fit_transform(data).toarray()
    perform_classification(data, fitness, features)


def perform_classification(data, fitness, features):
    clf = tree.DecisionTreeClassifier(max_depth=8)
    predictions = cross_val_predict(clf, data, fitness, cv=20)
    write_to_file(predictions, fitness, clf, features)


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


def write_to_file(predictions, fitness, classifier, features):
    filename = "outputdir/" + str(uuid.uuid1()) + ".txt"
    file = open(filename, "w")

    file.write(
        "Positive difference and the actual is lower than prediction. Negative and actual is higher than prediction.\n")
    file.write("Predictions: \n")
    np.savetxt(file, predictions.reshape(5, 20), fmt="%1.4f", delimiter=" ")
    file.write("\n")

    file.write("Actuals: \n")
    np.savetxt(file, fitness.reshape(5, 20), fmt="%1.4f", delimiter=" ")
    file.write("\n")

    differences = []
    for predict in range(0, len(predictions)):
        differences.append(predictions[predict] - fitness[predict])
    differences = np.asarray(differences).ravel()
    file.write("Differences: \n")
    np.savetxt(file, differences.reshape(5, 20), fmt="%1.4f", delimiter=" ")
    file.write("\n")
    file.write("Number of zeros: " + str(list(differences).count(0)))
    file.write("\n")
    file.write("Max-Depth: " + str(classifier.max_depth) + "\n")
    file.write("Features: " + str(features) + "\n")
    file.close()


if __name__ == "__main__":
    classification()
