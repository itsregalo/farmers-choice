from django import forms
from .models import *

class IssueSolutionForm(forms.ModelForm):
    class Meta:
        model = IssueSolution
        fields = ('description',)