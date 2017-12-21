from django import forms


class FitnessForm(forms.Form):
    def __init__(self, *args, **kwargs):
        size = kwargs.pop('size')
        super(FitnessForm, self).__init__(*args, **kwargs)

        for candidate in range(size):
            self.fields["fitness" + str(candidate)] = forms.IntegerField(max_value=10, min_value=0,
                                 widget=forms.NumberInput(attrs={"class": "fitness", "name": "fitness"}))


    def collectfitnesses(self):
        for name, fitness in self.cleaned_data.items():
            yield (self.fields[name], fitness)
