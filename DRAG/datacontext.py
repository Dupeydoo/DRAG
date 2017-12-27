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
    "systempath": os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
}
