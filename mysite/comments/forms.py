from django import forms
from .models import Cell

class CommentContributeForm(forms.Form):
    publisher_name = forms.CharField(label='名前')
    comment_text = forms.CharField(widget=forms.Textarea(), max_length=200, label='コメント')

class ThemeContributeForm(forms.Form):
    title = forms.CharField(label='タイトル')
    publisher_name = forms.CharField(label='名前')
    comment_zero = forms.CharField(widget=forms.Textarea(), max_length=200, label='コメント')