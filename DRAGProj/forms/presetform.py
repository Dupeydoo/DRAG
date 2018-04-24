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
    (2, "Rock-Three"),
    (3, "Alternative"),
    (4, "Alternative-Two")
)
"""
preset_choices (:obj:`tuple` of :obj:`tuple`): A list of available presets to 
use as input to the genetic algorithm.
"""


class PresetForm(forms.Form):
    """
    PresetForm serves as the class for the preset form. Pre-built tracks can
    be selected as inputs to the genetic algorithm.

    Attributes:
        preset (:obj:`TypedChoiceField`): A HTML5 Select object to allow the
        user to choose the preset desired.

        bpm (:obj:`IntegerField`): A HTML5 number input object to represent
        the bpm provided by the user.
    """
    preset = forms.TypedChoiceField(choices=preset_choices, coerce=int,
            widget=forms.Select(attrs={"class": "form-control cb"}))
    bpm = forms.IntegerField(max_value=250, min_value=60,
            widget=forms.NumberInput(attrs={"id": "bpmtwo", "name": "bpmtwo"}))

    def clean(self):
        """
        Server side validation of the preset form. Raises a validation error
        displaying a message on the page if validation fails.
        """
        cleaned_data = super().clean()

        if len(self.fields) == len(cleaned_data):
            bpm = cleaned_data["bpm"]
            preset = cleaned_data["preset"]

            # Check the bpm lies within the correct range.
            if bpm > 250 or bpm < 60:
                raise forms.ValidationError(
                    "BPM must be between 60 and 250."
                )

            # Checks the preset chosen is a valid preset.
            if preset < 0 or preset > (len(preset_choices) - 1) \
                    or not isinstance(preset, int):
                raise forms.ValidationError(
                    "Please choose one of the available presets."
                )

        else:
            raise forms.ValidationError("One of the fields was not submitted!")
