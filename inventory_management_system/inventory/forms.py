from django import forms
from .models import *

class PenForm(forms.ModelForm):
    class Meta:
        model = Pen
        fields = ('type', 'price', 'status', 'issues')

class NotebookForm(forms.ModelForm):
    class Meta:
        model = Notebook
        fields = ('type', 'price', 'status', 'issues')

class PencilcaseForm(forms.Form):
    class Meta:
        model = Pencilcase
        fields = ('type', 'price', 'status', 'issues')
