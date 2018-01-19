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
    "input_range": range(8),
    "manual_generations": 10,
    "automated_generations": 200,
    "current_generation": 1,
    "population_size": 10,
    "copy_ratio": 0.2,
    "tournament_size": 5,
    "time_signature": 8,  # two bars at 4:4
    "cross_prob": 0.5,
    "muta_prob": 0.4,
    "is_home": False,
    "system_path": os.path.dirname(os.path.dirname(os.path.abspath(__file__))),  # Location of the DRAG directory
    "wav_path": "/DRAG/static/wavfiles/",
    "presets": [[2, 1, 3, 1, 2, 1, 3, 1], [2, 2, 3, 1, 2, 2, 3, 1], [2, 2, 3, 2, 2, 2, 3, 1]]
}
"""
context (:obj:`dict`): Context containing algorithm parameters.
"""
