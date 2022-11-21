from django import forms
from .models import Cell


class ContributeForm(forms.Form):
    publisher_name = forms.CharField(label='名前')
    comment_text = forms.CharField(widget=forms.Textarea(), max_length=200, label='コメント')