import numpy as np

from DRAGNN.storage import datastore as ds
from DRAGNN.machinelearning import automategeneration as ag
from DRAG.datacontext import context

from sklearn import preprocessing
from sklearn.model_selection import GridSearchCV
from sklearn import ensemble
import uuid

HIGH_FITNESS_DIVIDE = 7
MID_FITNESS_DIVIDE = 4

HIGH_FITNESS_CLASS = 2
MID_FITNESS_CLASS = 1
LOW_FITNESS_CLASS = 0

TREE_DEPTH = 8
CROSS_VAL_FOLDS = 10
FEATURE_VALUES = 17


def classification(request, user_id):
    time_sig = context["time_signature"]
    ml_data = ds.read_data(time_sig, user_id)
    split_data(ml_data, request)


def split_data(ml_data, request):
    data = ml_data[0]
    features = len(data[0])
    fitness = decompose_fitness(ml_data[1].ravel())

    enc = preprocessing.OneHotEncoder(n_values=FEATURE_VALUES)
    data = enc.fit_transform(data).toarray()
    perform_classification(data, fitness, features, request, enc)


def perform_classification(data, fitness, features, request, hot_encoder):
    tuned_parameters = {"n_estimators": [10], "max_depth": [5, 8, 12], "min_samples_leaf": [3, 5, 8]}
    clf = GridSearchCV(ensemble.RandomForestClassifier(n_jobs=-1), tuned_parameters, n_jobs=-1, cv=CROSS_VAL_FOLDS)
    clf.fit(data, fitness)
    predictions = clf.predict(data)
    # write_to_file(predictions, fitness, features)
    ag.run(clf, request, hot_encoder)


def decompose_fitness(fitnesses):
    for fitness in range(len(fitnesses)):
        fitness_val = fitnesses[fitness]
        if fitness_val >= HIGH_FITNESS_DIVIDE:
            fitnesses[fitness] = HIGH_FITNESS_CLASS
        elif MID_FITNESS_DIVIDE <= fitness_val < HIGH_FITNESS_DIVIDE:
            fitnesses[fitness] = MID_FITNESS_CLASS
        else:
            fitnesses[fitness] = LOW_FITNESS_CLASS
    return fitnesses


def write_to_file(predictions, fitness, features):
    filename = context["system_path"] + "/DRAGNN/machinelearning/outputdir/" + str(uuid.uuid1()) + ".txt"
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
    file.write("Max-Depth: Determined by GridSearchCV\n")
    file.write("Features: " + str(features) + "\n")
    file.write("Cross-Val Folds: " + str(CROSS_VAL_FOLDS))
    file.close()


if __name__ == "__main__":
    classification("")
