import numpy as np
import math

from DRAGNN.storage import datastore as ds
from DRAG.datacontext import context

from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process import kernels
from sklearn import preprocessing
from sklearn import metrics
from matplotlib import pyplot as plt


def gaussian_regression():
    time_sig = context["time_signature"]
    ml_data = ds.read_data(time_sig, ds.get_data_store())
    split_data(ml_data)


def split_data(ml_data):
    data = ml_data[0]  # reshape X into numpy array of 100 samples of 1 feature.
    fitness = ml_data[1].ravel()  # flatten y values into single array.

    training_data = data[:-20]       # separate training and testing data.
    training_fitness = fitness[:-20]

    testing_data = data[-20:]
    testing_fitness = fitness[-20:]

    training_data = preprocessing.scale(training_data)   # scale the data
    testing_data = preprocessing.scale(testing_data)

    perform_regression(training_data, training_fitness, testing_data, testing_fitness)


def perform_regression(training_data, training_fitness, testing_data, testing_fitness):
    kernel = 1 ** 2 * kernels.RBF(length_scale=1, length_scale_bounds=(1e-2, 1e3))
    gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=5, alpha=1, normalize_y=True).fit(
        training_data, training_fitness)
    y_pred, sigma = gp.predict(testing_data, return_std=True)
    print(y_pred)
    print(testing_fitness)
    print("\n")
    log_regression_model(gp, testing_data, testing_fitness)
    # plot_results(training_data, training_fitness, testing_data, gp)


def log_regression_model(model, testing_data, testing_fitness):
    msq = metrics.mean_squared_error(model.predict(testing_data), testing_fitness)
    print("Mean Squared Error: " + str(msq))
    print("Root Mean Squared Error: " + str(math.sqrt(msq)))
    print("R2 Score: " + str(model.score(testing_data, testing_fitness)))


def plot_results(training_data, training_fitness, testing_data, model):
    plt.scatter(training_data, training_fitness, color='g')
    plt.plot(testing_data, model.predict(testing_data), color='k')
    plt.show()


if __name__ == "__main__":
    gaussian_regression()
