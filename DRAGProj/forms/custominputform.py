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

instrumentchoices = (
    (1, "Hi-Hat"),
    (2, "Snare Drum"),
    (3, "Kick Drum"),
    (4, "High-Tom"),
    (5, "Hi-Hat and High-Tom"),
    (6, "Hi-Hat, High-Tom and Snare"),
    (7, "Hi-Hat and Kick"),
    (8, "Hi-Hat, Kick and High-Tom"),
    (9, "Hi-Hat, Kick and Snare"),
    (10, "All Instruments"),
    (11, "Hi-Hat and Snare"),
    (12, "High-Tom and Snare"),
    (13, "Hi-Tom, Snare and Kick"),
    (14, "Kick and High-Tom"),
    (15, "Kick and Snare"),
    (16, "Play Nothing")
)
"""
instrumentchoices (:obj:`tuple` of :obj:`tuple`): The choices to be visible on the input dropdowns.
"""

genres = [
    ("Rock", "Rock"),
    ("Jazz", "Jazz"),
    ("Blues", "Blues")
]
"""
genres (:obj:`list` of :obj:`tuple`): The choices of genre for the input dropdown.
"""


class CustomInputForm(forms.Form):
    """
    The CustomInputForm class has fields for each beat of a 2 bar crotchet 4:4 timesig track
    where the user may create a custom track from a selection of instruments.

    Attributes:
        beat + number (:obj:`TypedChoiceField`): Each beat has its own dropdown object using a HTML5 Select.
        bpm (:obj:`IntegerField`): An object representing a HTML5 number input for the bpm.
        genre (:obj:`ChoiceField`): An object representing a HTML5 dropdown for choosing track genre.
    """
    beatone = forms.TypedChoiceField(choices=instrumentchoices, coerce=int, widget=forms.Select(attrs={"class": "form-control cb"}))
    beattwo = forms.TypedChoiceField(choices=instrumentchoices, coerce=int, widget=forms.Select(attrs={"class": "form-control cb"}))
    beatthree = forms.TypedChoiceField(choices=instrumentchoices, coerce=int, widget=forms.Select(attrs={"class": "form-control cb"}))
    beatfour = forms.TypedChoiceField(choices=instrumentchoices, coerce=int, widget=forms.Select(attrs={"class": "form-control cb"}))
    beatfive = forms.TypedChoiceField(choices=instrumentchoices, coerce=int, widget=forms.Select(attrs={"class": "form-control cb"}))
    beatsix = forms.TypedChoiceField(choices=instrumentchoices, coerce=int, widget=forms.Select(attrs={"class": "form-control cb"}))
    beatseven = forms.TypedChoiceField(choices=instrumentchoices, coerce=int, widget=forms.Select(attrs={"class": "form-control cb"}))
    beateight = forms.TypedChoiceField(choices=instrumentchoices, coerce=int, widget=forms.Select(attrs={"class": "form-control cb"}))
    bpm = forms.IntegerField(max_value=250, min_value=1,
                             widget=forms.NumberInput(attrs={"id": "bpm", "name": "bpm"}))
    genre = forms.ChoiceField(choices=genres, widget=forms.Select(attrs={"class": "form-control", "id": "genre"}))
