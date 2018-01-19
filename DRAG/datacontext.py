import os

"""
The Datacontext module contains a dictionary which houses algorithm parameters and other useful
information used when DRAG runs. 

    author:
        James
        
    version:
        1.7.5    
"""

context = {
    "inputrange": range(8),
    "manualgenerations": 10,
    "currentgeneration": 1,
    "populationsize": 10,
    "copyratio": 0.2,
    "tournamentsize": 5,
    "timesignature": 8,  # two bars at 4:4
    "crossprob": 0.5,
    "mutaprob": 0.4,
    "is_home": False,
    "systempath": os.path.dirname(os.path.dirname(os.path.abspath(__file__))),  # Location of the DRAG directory
    "wavpath": "/DRAG/static/wavfiles/",
    "presets": [[2, 1, 3, 1, 2, 1, 3, 1], [2, 2, 3, 1, 2, 2, 3, 1], [2, 2, 3, 2, 2, 2, 3, 1]]
}
"""
context (:obj:`dict`): Context containing algorithm parameters.
"""
