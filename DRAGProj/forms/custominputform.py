from django import forms

"""
A module containing the form class and recipes to make the custom beat input form.

    Author:
        James
        
    Version:
        1.0.0
        
    See:
        forms.Form,
        DRAGProj.views
"""

instrument_choices = (
    (1, "Hi-Hat"),
    (2, "Hi-Hat and Kick"),
    (3, "Hi-Hat and Snare"),
    (4, "Snare Drum"),
    (5, "Kick Drum"),
    (6, "Kick and Snare"),
    (7, "High-Tom Drum"),
    (8, "Kick and High-Tom"),
    (9, "Hi-Hat and High-Tom"),
    (10, "High-Tom and Snare"),
    (11, "Play Nothing"),
    (12, "High-Hat, Kick and Snare"),
    (13, "Hi-Hat, Kick and High-Tom"),
    (14, "High-Tom, Snare and Kick"),
    (15, "Hi-Hat, High-Tom and Snare"),
    (16, "All Instruments")
)
"""
instrument_choices (:obj:`tuple` of :obj:`tuple`): The choices to be visible on the input drop-downs.
"""

genres = [
    ("Rock", "Rock"),
    ("Jazz", "Jazz"),
    ("Blues", "Blues")
]
"""
genres (:obj:`list` of :obj:`tuple`): The choices of genre for the input drop-down.
"""


class CustomInputForm(forms.Form):
    """
    The CustomInputForm class has fields for each beat of a 2 bar crotchet 4:4 time_sig track
    where the user may create a custom track from a selection of instruments.

    Attributes:
        beat + number (:obj:`TypedChoiceField`): Each beat has its own drop-down object using a HTML5 Select.
        bpm (:obj:`IntegerField`): An object representing a HTML5 number input for the bpm.
        genre (:obj:`ChoiceField`): An object representing a HTML5 drop-down for choosing track genre.
    """
    beat_one = forms.TypedChoiceField(choices=instrument_choices, coerce=int,
                                      widget=forms.Select(attrs={"class": "form-control cb"}))
    beat_two = forms.TypedChoiceField(choices=instrument_choices, coerce=int,
                                      widget=forms.Select(attrs={"class": "form-control cb"}))
    beat_three = forms.TypedChoiceField(choices=instrument_choices, coerce=int,
                                        widget=forms.Select(attrs={"class": "form-control cb"}))
    beat_four = forms.TypedChoiceField(choices=instrument_choices, coerce=int,
                                       widget=forms.Select(attrs={"class": "form-control cb"}))
    beat_five = forms.TypedChoiceField(choices=instrument_choices, coerce=int,
                                       widget=forms.Select(attrs={"class": "form-control cb"}))
    beat_six = forms.TypedChoiceField(choices=instrument_choices, coerce=int,
                                      widget=forms.Select(attrs={"class": "form-control cb"}))
    beat_seven = forms.TypedChoiceField(choices=instrument_choices, coerce=int,
                                        widget=forms.Select(attrs={"class": "form-control cb"}))
    beat_eight = forms.TypedChoiceField(choices=instrument_choices, coerce=int,
                                        widget=forms.Select(attrs={"class": "form-control cb"}))
    bpm = forms.IntegerField(max_value=250, min_value=60,
                             widget=forms.NumberInput(attrs={"id": "bpm", "name": "bpm"}))
    genre = forms.ChoiceField(choices=genres, widget=forms.Select(attrs={"class": "form-control", "id": "genre"}))

    def clean(self):
        cleaned_data = super().clean()
        bpm = cleaned_data["bpm"]

        for key, value in cleaned_data.items():
            if "beat" in key:
                if value < 1 or value > 16 or not isinstance(value, int):
                    raise forms.ValidationError(
                        str(key) + " was given an incorrect value."
                    )

        if bpm > 250 or bpm < 60:
            raise forms.ValidationError(
                "BPM must be between 60 and 250."
            )
