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
    "manual_generations": 10,
    "automated_generations": 200,
    "population_size": 10,
    "copy_ratio": 0.2,
    "tournament_size": 2,
    "time_signature": 8,  # two bars at 4:4
    "cross_prob": 0.6,
    "muta_prob": 0.6,
    "is_home": False,
    "system_path": os.path.dirname(os.path.dirname(os.path.abspath(__file__))),  # Location of the DRAG directory
    "wav_path": "/DRAG/static/wavfiles/"
}
"""
context (:obj:`dict`): Context containing algorithm parameters.
"""
