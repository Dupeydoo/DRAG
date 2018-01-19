from django import forms

"""
A module housing the form used for rating track fitness.

    Author:
        James
    
    Version:
        2.0.0
        
    See:
        forms.Form,
        DRAGProj.views
"""


class FitnessForm(forms.Form):
    """
    The FitnessForm class serves as the main form the user uses to rate tracks over generations.

    Attributes:
        fields (:obj:`dict`): Form fields collection, containing the form fields explicitly.
    """

    def __init__(self, *args, **kwargs):
        """
        FitnessForm constructor.

        Args:
            **kwargs (:obj:`dict`): The dictionary of additional keyword arguments provided.
        """
        size = kwargs.pop('size')  # Pop off the size keyword argument.
        super(FitnessForm, self).__init__(*args, **kwargs)  # Call the forms.Form constructor.

        for candidate in range(size):
            # Create IntegerFields dynamically based on how many population members there are.
            self.fields["fitness" + str(candidate)] = forms.IntegerField(max_value=10,
                                                                         min_value=0,
                                                                         widget=forms.NumberInput(
                                                                             attrs={"class": "fitness",
                                                                                    "name": "fitness",
                                                                                    "tabindex": size + 1}))

    def collect_fitnesses(self):
        """
        This method collects the cleaned fitness inputs ready for assignment.

        Yields:
            (name, fitness) (:obj:`tuple`): name, fitness pairs from the cleaned data dictionary. The yield creates
            a generator object to use for assignment.
        """
        for name, fitness in self.cleaned_data.items():  # This forms cleaned items.
            yield (self.fields[name], fitness)
