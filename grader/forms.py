from django import forms
from .models import Question, Essay

class AnswerForm(forms.ModelForm):
    answer = forms.CharField(max_length=100000, widget=forms.Textarea(attrs={'rows': 5, 'placeholder': "Enter assignment submission text here"}))
    matric = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': "Enter your matric number"}))
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': "Enter your name"}))

    class Meta:
        model = Essay
        fields = ['answer', 'matric', 'name']
