from DRAG.datacontext import context
from DRAGProj import geneticrunner as gr
import numpy as np


def run(model, request, hot_encoder):
    for generation in range(context["automated_generations"]):
        request.session["current_generation"] += 1
        print(request.session["current_generation"])
        single_generation(model, request, hot_encoder)

    for member in context[request.session["user_id"] + "population"]:
        print(member.fitness)


def single_generation(model, request, hot_encoder):
    for track in context[request.session["user_id"] + "population"]:
        drums = np.array([track.content])
        content = hot_encoder.transform(drums).toarray()
        track.fitness = model.predict(content)

    context[request.session["user_id"] + "population"] = gr.perform_genetics(
        context[request.session["user_id"] + "population"])


if __name__ == "__main__":
    from DRAGTests.mock.mockpopulation import MockPopulation
    from DRAGNN.storage import datastore as ds
    from DRAGNN.machinelearning.classification import decompose_fitness

    from sklearn import preprocessing
    from sklearn import ensemble
    from sklearn import model_selection

    mock = MockPopulation().population


    class Request:
        def __init__(self):
            self.session = {}


    request_test = Request()
    request_test.session["current_generation"] = 10
    request_test.session["user_id"] = ""
    context["population"] = mock

    ml_data = ds.read_data(8, "")
    data = ml_data[0]

    fitness_test = decompose_fitness(ml_data[1].ravel())
    enc = preprocessing.OneHotEncoder(n_values=17)
    data = enc.fit_transform(data).toarray()

    tuned_parameters = {"n_estimators": [10], "max_depth": [5, 8, 12], "min_samples_leaf": [3, 5, 8]}
    clf = model_selection.GridSearchCV(ensemble.RandomForestClassifier(n_jobs=-1), tuned_parameters, n_jobs=-1, cv=10)
    clf.fit(data, fitness_test)

    run(clf, request_test, enc)
