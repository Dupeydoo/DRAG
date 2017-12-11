from django import forms

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


class CustomInputForm(forms.Form):
    custombeat = forms.ChoiceField(choices=instrumentchoices, widget=forms.Select(attrs={"class": "form-control"}))
    bpm = forms.IntegerField(label="Enter a BPM: ", max_value=250, min_value=1,
                             widget=forms.NumberInput(attrs={"id": "bpm", "name": "bpm"}))
