from django import forms

"""
This module houses the simple PresetForm used for ease of the user.

    Author:
        James
    
    Version:
        1.0.0
        
    See:
        forms.Form
"""

preset_choices = (
    (0, "Rock"),
    (1, "Rock-Two"),
    (2, "Rock-Three")
)
"""
preset_choices (:obj:`tuple` of :obj:`tuple`): A list of available presets to 
use as input to the genetic algorithm.
"""


class PresetForm(forms.Form):
    """
    PresetForm serves as the class for the preset form. Pre-built tracks can be selected as inputs to the
    genetic algorithm.

    Attributes:
        preset (:obj:`TypedChoiceField`): A HTML5 Select object to allow the user to choose the preset desired.
        bpm (:obj:`IntegerField`): A HTML5 number input object to represent the bpm provided by the user.
    """
    preset = forms.TypedChoiceField(choices=preset_choices, coerce=int,
                                    widget=forms.Select(attrs={"class": "form-control cb"}))
    bpm = forms.IntegerField(max_value=250, min_value=1,
                             widget=forms.NumberInput(attrs={"id": "bpmtwo", "name": "bpmtwo"}))
