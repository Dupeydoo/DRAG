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
    "manual_generations": 10,                                                    # Number of manual generations to run.
    "automated_generations": 100,                                                # Number of automated generations ran.
    "population_size": 10,                                                       # Size of the GA population.
    "copy_ratio": 0.2,                                                           # Number of copies to create initially.
    "tournament_size": 2,                                                        # Tournament selection parameter.
    "time_signature": 8,                                                         # In this case total beats in two bars.
    "cross_prob": 0.6,                                                           # The probability of crossover.
    "muta_prob": 0.6,                                                            # The probability of mutation.
    "is_home": False,                                                            # Helps control the menu options.
    "system_path": os.path.dirname(os.path.dirname(os.path.abspath(__file__))),  # Location of the DRAG directory
    "wav_path": "/DRAG/static/wavfiles/"                                         # Location of the server wav files.
}
"""
context (:obj:`dict`): Context containing algorithm parameters.
"""
