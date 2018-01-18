from sklearn import linear_model
import numpy as np

from DRAGNN.storage import datastore as ds
from DRAG.datacontext import context


def linearregression():
    timesig = context["timesignature"]
    mldata = ds.readData(timesig, ds.getdatastore())
    splitdata(mldata)


def splitdata(mldata):
    data = mldata[0]
    fitness = mldata[1]

    training_data = data[:-20]
    training_fitness = fitness[:-20]

    testing_data = data[-20:]
    testing_fitness = data[-20:]
    performregression(training_data, training_fitness, testing_data, testing_fitness)


def performregression(training_data, training_fitness, testing_data, testing_fitness):
    regr = linear_model.LinearRegression()
    regr.fit(training_data, training_fitness)

    print(regr.coef_)

    msq = np.mean((regr.predict(testing_data) - testing_fitness)) ** 2
    print(msq)
    print(regr.score(testing_data, testing_fitness))
