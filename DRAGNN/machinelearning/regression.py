from sklearn import linear_model
from sklearn.feature_selection import SelectKBest, chi2
import numpy as np
import math

from DRAGNN.storage import datastore as ds
from DRAGNN.machinelearning import automategeneration as ag
from DRAG.datacontext import context


def linearregression():
    timesig = context["timesignature"]
    mldata = ds.readData(timesig, ds.getdatastore())
    splitdata(mldata)


def splitdata(mldata):
    data = mldata[0]
    fitness = mldata[1].ravel()

    # data_new = SelectKBest(chi2, k=4).fit_transform(data, fitness)
    # data = np.tile(data, (10, 1))
    # fitness = np.tile(fitness, 10)

    training_data = data[:-20]
    training_fitness = fitness[:-20]

    testing_data = data[-20:]
    testing_fitness = fitness[-20:]
    performregression(training_data, training_fitness, testing_data, testing_fitness)


def performregression(training_data, training_fitness, testing_data, testing_fitness):
    regr = linear_model.HuberRegressor()
    regr.fit(training_data, training_fitness)
    logregressionmodel(regr, testing_data, testing_fitness)
    if 1 == 0:
        ag.run(regr)


def logregressionmodel(model, testing_data, testing_fitness):
    print("Regression Coefficients:\n")
    print(model.coef_)
    msq = np.mean((model.predict(testing_data) - testing_fitness)) ** 2
    print("Mean Squared Error: " + str(msq))
    print("Root Mean Squared Error: " + str(math.sqrt(msq)))
    print("Coefficient of Determination: " + str(model.score(testing_data, testing_fitness)))
    print("Predict with a nice rock rhythm: " + str(model.predict([[2, 1, 3, 1, 2, 1, 3, 1]])))
    print("Predict with a rather useless rhythm: " + str(model.predict([[11, 11, 11, 11, 11, 11, 11, 11]])))


if __name__ == "__main__":
    linearregression()
