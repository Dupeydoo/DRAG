"""
The drummapper module exposes the dictionary of possible DRAG instruments
that can be used. Each numeric value corresponds to a key filename which
can be used to located the wav file.

    Author:
        James

    Version:
        1.0.0
"""

drum_mapper = {
    1: "HHat.wav",
    2: "HHatKick.wav",
    3: "HHatSnare.wav",
    4: "Snare.wav",
    5: "Kick.wav",
    6: "KickSnare.wav",
    7: "HTom.wav",
    8: "KickHTom.wav",
    9: "HHatHTom.wav",
    10: "HTomSnare.wav",
    11: "PlayNothing.wav",
    12: "HHatKickSnare.wav",
    13: "HHatKickHTom.wav",
    14: "HTomSnareKick.wav",
    15: "HHatHTomSnare.wav",
    16: "HHatKickSnareHTom.wav"
}
"""
drum_mapper (:obj:`dict` of int keys and :obj:`str` values): The drum_mapper 
dictionary.
"""


def is_cymbal(drum):
    """
    Checks the drum to see if it is a cymbal, namely a HiHat.

    Args:
        drum (int): The dictionary key corresponding to a drum.

    Returns:
        bool: True if it is a cymbal, False if not.
    """
    return "HHat" in drum_mapper[drum]
