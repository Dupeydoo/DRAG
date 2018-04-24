from DRAGProj.models.preset import Preset

"""
A module which assists the beat input form in
constructing the algorithm input.

    Author:
        James
        
    Version:
        2.0.0
        
    See:
        DRAG.datacontext
        DRAGProj.views
"""


def construct_input(cleaned_data):
    """
    A function to collect the clean form data and
    populate a list with it.

    Args:
        cleaned_data (:obj:`dict` of :obj:`str` keys and int values):
        The valid form data.

    Returns:
        input_list (:obj:`list` of int): The input list to the algorithm.

    """
    input_list = [cleaned_data["beat_one"], cleaned_data["beat_two"],
                  cleaned_data["beat_three"], cleaned_data["beat_four"],
                  cleaned_data["beat_five"], cleaned_data["beat_six"],
                  cleaned_data["beat_seven"], cleaned_data["beat_eight"]]
    return input_list


def get_preset(index):
    """
    An accessor function to get a preset from the database based on its
    index.

    Args:
        index (int): Index of preset.

    Returns:
        :obj:`list` of int: The preset list.

    See:
        DRAG.datacontext
    """
    # Get the preset using a database model.
    preset_from_db = Preset.objects.get(pk=index + 1)
    return [preset_from_db.beat_one, preset_from_db.beat_two,
            preset_from_db.beat_three, preset_from_db.beat_four,
            preset_from_db.beat_five, preset_from_db.beat_six,
            preset_from_db.beat_seven, preset_from_db.beat_eight]

