from django import forms
from .models import *

class IssueSolutionForm(forms.ModelForm):
    class Meta:
        model = IssueSolution
        fields = ('description',)
class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('title', 'description', 'category', 'image')
        