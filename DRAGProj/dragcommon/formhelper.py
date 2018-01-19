import DRAG.datacontext as dc

"""
A module which assists the beat input form in
constructing the algorithm input.

    Author:
        James
        
    Version:
        2.0.0
        
    See:
        DRAG.datacontext.py
        DRAGProj.views
"""


def construct_input(cleaned_data):
    """
    A function to collect the clean form data and
    populate a list with it.

    Args:
        cleaned_data (:obj:`dict` of :obj:`str` keys and int values): The valid form data.

    Returns:
        input_list (:obj:`list` of int): The input list to the algorithm.

    """
    input_list = []
    input_list.append(cleaned_data["beat_one"])
    input_list.append(cleaned_data["beat_two"])
    input_list.append(cleaned_data["beat_three"])
    input_list.append(cleaned_data["beat_four"])
    input_list.append(cleaned_data["beat_five"])
    input_list.append(cleaned_data["beat_six"])
    input_list.append(cleaned_data["beat_seven"])
    input_list.append(cleaned_data["beat_eight"])
    return input_list


def get_preset(index):
    """
    An accessor function to get a preset based on its index.

    Args:
        index (int): Index of preset.

    Returns:
        :obj:`list` of int: The preset list.

    See:
        DRAG.datacontext
    """
    return dc.context["presets"][index]
