import numpy as np
import math

from DRAGNN.storage import datastore as ds
from DRAGNN.machinelearning import automategeneration as ag
from DRAG.datacontext import context
from DRAGTests.mock.mockpopulation import MockPopulation

from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel
from sklearn import preprocessing


def gaussian_regression():
    time_sig = context["time_signature"]
    ml_data = ds.read_data(time_sig, ds.get_data_store())
    split_data(ml_data)


def split_data(ml_data):
    data = ml_data[0]
    scaled_data = preprocessing.scale(data)
    fitness = ml_data[1].ravel()

    # scaled_data = np.tile(scaled_data, (10, 1))
    # fitness = np.tile(fitness, 10)

    training_data = scaled_data[:-20]
    training_fitness = fitness[:-20]

    # training_data, training_fitness = augment_data(training_data, training_fitness)

    testing_data = scaled_data[-20:]
    testing_fitness = fitness[-20:]
    perform_regression(training_data, training_fitness, testing_data, testing_fitness)


def perform_regression(training_data, training_fitness, testing_data, testing_fitness):
    kernel = 1.0 * RBF(length_scale=8.0, length_scale_bounds=(1e-2, 1e3)) \
             + WhiteKernel(noise_level=1, noise_level_bounds=(1e-1, 1e2))

    gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=5, alpha=0.0, normalize_y=True).fit(
        training_data, training_fitness)
    y_pred, sigma = gp.predict(testing_data, return_std=True)
    print(y_pred)
    print("\n")
    log_regression_model(gp, testing_data, testing_fitness)


def log_regression_model(model, testing_data, testing_fitness):
    msq = np.mean((model.predict(testing_data) - testing_fitness)) ** 2
    print("Mean Squared Error: " + str(msq))
    print("Root Mean Squared Error: " + str(math.sqrt(msq)))
    print("R2 Score: " + str(model.score(testing_data, testing_fitness)))


def augment_data(training_data, training_fitness):
    mu, sigma = 0, 0.5
    data_dim = 80
    for aug in range(10):
        data_noise = np.random.normal(mu, sigma, [data_dim, 8])
        fitness_noise = np.random.normal(mu, sigma, [data_dim])
        data_aug = training_data[-data_dim:] + data_noise
        fitness_aug = training_fitness[-data_dim] + fitness_noise
        training_data = np.concatenate((training_data, data_aug))
        training_fitness = np.concatenate((training_fitness, fitness_aug))
    return training_data, training_fitness


if __name__ == "__main__":
    gaussian_regression()
