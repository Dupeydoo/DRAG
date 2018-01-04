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


def constructinput(cleaned_data):
    """
    A function to collect the clean form data and
    populate a list with it.

    Args:
        cleaned_data (:obj:`dict` of :obj:`str` keys and int values): The valid form data.

    Returns:
        input (:obj:`list` of int): The input list to the algorithm.

    """
    input = []
    input.append(cleaned_data["beatone"])
    input.append(cleaned_data["beattwo"])
    input.append(cleaned_data["beatthree"])
    input.append(cleaned_data["beatfour"])
    input.append(cleaned_data["beatfive"])
    input.append(cleaned_data["beatsix"])
    input.append(cleaned_data["beatseven"])
    input.append(cleaned_data["beateight"])
    return input


def getpreset(index):
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
