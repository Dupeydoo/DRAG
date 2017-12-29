import os

context = {
    "inputrange": range(8),
    "manualgenerations": 10,
    "currentgeneration": 1,
    "populationsize": 10,
    "copyratio": 0.4,
    "tournamentsize": 5,
    "timesignature": 8,  # two bars at 4:4
    "crossprob": 0.5,
    "mutaprob": 0.4,
    "is_home": False,
    "systempath": os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "presets": [[7, 1, 11, 1, 7, 1, 11, 1], [7, 7, 11, 1, 1, 11, 1, 1], [7, 7, 11, 7, 7, 7, 11, 1]]
}
