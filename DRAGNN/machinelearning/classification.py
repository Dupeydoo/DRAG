import numpy as np

from DRAGNN.storage import datastore as ds
from DRAGNN.machinelearning import automategeneration as ag
from DRAG.datacontext import context

from sklearn import preprocessing
from sklearn.model_selection import GridSearchCV
from sklearn import ensemble
import uuid

HIGH_FITNESS_DIVIDE = 7
"""
HIGH_FITNESS_DIVIDE (int): The boundary by which high fitness candidates are categorised.
"""
MID_FITNESS_DIVIDE = 4
"""
MID_FITNESS_DIVIDE (int): The boundary by which medium fitness candidates are categorised.
"""

HIGH_FITNESS_CLASS = 2
"""
HIGH_FITNESS_CLASS (int): The fitness class representation for highly rated candidates.
"""
MID_FITNESS_CLASS = 1
"""
MID_FITNESS_CLASS (int): The fitness class representation for medium rated candidates.
"""
LOW_FITNESS_CLASS = 0
"""
LOW_FITNESS_CLASS (int): The fitness class representation for low rated candidates.
"""

TREE_DEPTH = 8
"""
TREE_DEPTH (int): How many levels to expand a decision tree within the Random Forest Classifier.
"""
CROSS_VAL_FOLDS = 10
"""
CROSS_VAL_FOLDS (int): The number of times to fold training data with Cross Validation.
"""
FEATURE_VALUES = 17
"""
FEATURE_VALUES (int): The amount of possible feature values, 0 to 16 inclusive.
"""


def classification(request, user_id):
    """
    Entry function to the classification process, reads the
    time signature and initiates data processing.

    Args:
        request (:obj:`Request`): The request object needed to
        automate generations.

        user_id (:obj:`str`): The user's string identifier.
    """
    time_sig = context["time_signature"]

    # Read the data from the datastore module.
    ml_data = ds.read_data(time_sig, user_id)
    split_data(ml_data, request)


def split_data(ml_data, request):
    """
    Splits the HDF5 data into tracks and fitnesses. Also
    performs OHE on tracks.

    Args:
        ml_data (:obj:`tuple` of :obj:`ndarray`): Data read in
        from the datastore.

        request (:obj:`Request`): The request object needed to
        automate generations.
    """
    data = ml_data[0]
    features = len(data[0])

    # Translate original fitness values into the 0, 1, 2 fitness
    # class scheme.
    fitness = decompose_fitness(ml_data[1].ravel())

    enc = preprocessing.OneHotEncoder(n_values=FEATURE_VALUES)
    data = enc.fit_transform(data).toarray()
    perform_classification(data, fitness, features, request, enc)


def perform_classification(data, fitness, features, request, hot_encoder):
    """
    Performs classification with a RFC and GridSearchCV. Automatic generations
    are then ran.

    Args:
        data (:obj:`ndarray`): Track data in a matrix like numpy array.
        fitness (:obj:`fitness`): Fitness data in a numpy array.
        features (int): The number of features per sample. Used in write_to_file when called.
        request (:obj:`Request`): The request object used in automating generations.
        hot_encoder (:obj:`OneHotEncoder`: The OHE used to encode future tracks.
    """

    # Establish a parameter set for GridSearchCV to search.
    tuned_parameters = {"n_estimators": [10], "max_depth": [5, 8, 12], "min_samples_leaf": [3, 5, 8]}

    # Perform parallelised GridSearchCV and RFC and fit the model.
    clf = GridSearchCV(ensemble.RandomForestClassifier(n_jobs=-1), tuned_parameters, n_jobs=-1, cv=CROSS_VAL_FOLDS)
    clf.fit(data, fitness)

    # Run the automated generations.
    ag.run(clf, request, hot_encoder)


def decompose_fitness(fitnesses):
    """
    Translates the fitness ratings from manual generations into the
    categorical format used in the classification process.

    Args:
        fitnesses (:obj:`ndarray`): A flat ndarray containing all the
        fitness values.

    Returns:
        fitnesses (:obj:`ndarray`): The translated fitness values.
    """
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
    """
    File writing function used to collect machine learning criteriton
    results. Call in perform_classification to record results. You must
    pass the function a matrix of predictions obtained with the scikit learn
    predict function.

    The output file is written to ./outputdir

    Args:
        predictions (:obj:`ndarray`): Predictions on the training data.
        fitness (:obj:`ndarray`): Actual training fitness data.
        features (int): The number of features sample.
    """
    filename = context["system_path"] + "/DRAGNN/machinelearning/outputdir/" \
               + str(uuid.uuid1()) + ".txt"
    file = open(filename, "w")

    # Predictions block. Data is reshaped into a presentable format.
    file.write(
        "Positive difference and the actual is lower than prediction."
        + " Negative and actual is higher than prediction.\n")
    file.write("Predictions: \n")
    np.savetxt(file, predictions.reshape(5, 20), fmt="%1.4f", delimiter=" ")
    file.write("\n")

    # Actuals block. Data is reshaped into a presentable format.
    file.write("Actuals: \n")
    np.savetxt(file, fitness.reshape(5, 20), fmt="%1.4f", delimiter=" ")
    file.write("\n")

    # Calculate the differences between predictions and actuals.
    differences = []
    for predict in range(0, len(predictions)):
        differences.append(predictions[predict] - fitness[predict])

    # Differences block.
    differences = np.asarray(differences).ravel()
    file.write("Differences: \n")
    np.savetxt(file, differences.reshape(5, 20), fmt="%1.4f", delimiter=" ")
    file.write("\n")

    # Metrics and parameters block.
    file.write("Number of zeros: " + str(list(differences).count(0)))
    file.write("\n")

    file.write("Max-Depth: Determined by GridSearchCV\n")
    file.write("Features: " + str(features) + "\n")
    file.write("Cross-Val Folds: " + str(CROSS_VAL_FOLDS))
    file.close()
