from django import forms
from .models import *

class IssueSolutionForm(forms.ModelForm):
    class Meta:
        model = IssueSolution
        fields = ('description',)

        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
        }
class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('title', 'description', 'category', )
        # add class="form-control" to each field
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'description': forms.Textarea(attrs={'class': 'form-control col-md-6'}),
            'category': forms.Select(attrs={'class': 'form-control col-md-6'}),}
        