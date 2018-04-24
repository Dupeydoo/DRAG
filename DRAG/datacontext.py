import os

"""
The Datacontext module contains a dictionary which houses algorithm 
parameters and other useful information used when DRAG runs. 

    author:
        James
        
    version:
        1.7.5    
"""

context = {
    # Number of manual generations to run.
    "manual_generations": 10,

    # Number of automated generations to run.
    "automated_generations": 100,

    # Size of the GA population.
    "population_size": 10,

    # Number of copies to create initially.
    "copy_ratio": 0.3,

    # Tournament selection parameter.
    "tournament_size": 4,

    # In this case total beats in two bars.
    "time_signature": 8,

    # The probability of crossover.
    "cross_prob": 0.3,

    # The probability of mutation.
    "muta_prob": 0.6,

    # Helps control the menu options.
    "is_home": False,

    # Location of the DRAG directory.
    "system_path": os.path.dirname(os.path.dirname(os.path.abspath(__file__))),

    # Location of the server wav files.
    "wav_path": "/DRAG/static/wavfiles/"
}
"""
context (:obj:`dict`): Context containing algorithm parameters.
"""
