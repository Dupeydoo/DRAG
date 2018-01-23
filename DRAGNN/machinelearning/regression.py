from sklearn import linear_model
from sklearn import ensemble
import numpy as np
import math

from DRAGNN.storage import datastore as ds
from DRAGNN.machinelearning import automategeneration as ag
from DRAG.datacontext import context

from DRAGTests.mock.mockpopulation import MockPopulation


def linear_regression():
    time_sig = context["time_signature"]
    ml_data = ds.read_data(time_sig, ds.get_data_store())
    split_data(ml_data)


def split_data(ml_data):
    data = ml_data[0]
    fitness = ml_data[1].ravel()

    # data_new = SelectKBest(chi2, k=4).fit_transform(data, fitness)
    data = np.tile(data, (10, 1))
    fitness = np.tile(fitness, 10)

    training_data = data[:-20]
    training_fitness = fitness[:-20]

    testing_data = data[-20:]
    testing_fitness = fitness[-20:]
    perform_regression(training_data, training_fitness, testing_data, testing_fitness)


def perform_regression(training_data, training_fitness, testing_data, testing_fitness):
    # regr = linear_model.RANSACRegressor(linear_model.LinearRegression())
    regr = ensemble.RandomForestRegressor(n_estimators=10, max_features=8)
    regr.fit(training_data, training_fitness)
    log_regression_model(regr, testing_data, testing_fitness)
    # ag.run(regr)


def log_regression_model(model, testing_data, testing_fitness):
    print("Regression Coefficients:\n")
    # print(model.coef_)
    msq = np.mean((model.predict(testing_data) - testing_fitness)) ** 2
    print("Mean Squared Error: " + str(msq))
    print("Root Mean Squared Error: " + str(math.sqrt(msq)))
    print(model.score(testing_data, testing_fitness))
    print("Predict with a nice rock rhythm: " + str(model.predict([[2, 1, 3, 1, 2, 1, 3, 1]])))
    print("Predict with a rather useless rhythm: " + str(model.predict([[11, 11, 11, 11, 11, 11, 11, 11]])))


if __name__ == "__main__":
    context["population"] = MockPopulation().population
    linear_regression()
