from django import forms

presetchoices = (
    (0, "Rock"),
    (1, "Rock-Two"),
    (2, "Rock-Three")
)

class PresetForm(forms.Form):
    preset = forms.TypedChoiceField(choices=presetchoices, coerce=int, widget=forms.Select(attrs={"class": "form-control cb"}))
    bpm = forms.IntegerField(max_value= 250, min_value=1, widget=forms.NumberInput(attrs={"id": "bpmtwo", "name": "bpmtwo"}))