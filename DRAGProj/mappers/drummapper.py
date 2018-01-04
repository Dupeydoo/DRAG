"""
The drummapper module exposes the dictionary of possible DRAG instruments
that can be used. Each numeric value corresponds to a key filename which
can be used to located the wav file.

    Author:
        James

    Version:
        1.0.0
"""

drummapper = {
    1: "HHat.wav",
    2: "Snare.wav",
    3: "Kick.wav",
    4: "HTom.wav",
    5: "HHatHTom.wav",
    6: "HHatHtomSnare.wav",
    7: "HHatKick.wav",
    8: "HHatKickHTom.wav",
    9: "HHatKickSnare.wav",
    10: "HHatKickSnareHTom.wav",
    11: "HHatSnare.wav",
    12: "HTomSnare.wav",
    13: "HTomSnareKick.wav",
    14: "KickHTom.wav",
    15: "KickSnare.wav",
    16: "PlayNothing.wav"
}
"""
drummapper (:obj:`dict` of int keys and :obj:`str` values): The drummapper dictionary.
"""

def isSymbal(drum):
    """
    Checks the drum to see if it is a symbal, namely a HiHat.

    Args:
        drum (int): The dictionary key corresponding to a drum.

    Returns:
        bool: True if it is a symbal, False if not.
    """
    return "HHat" in drummapper[drum]
