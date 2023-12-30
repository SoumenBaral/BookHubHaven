from django import forms
from . import models

class AddCarForm(forms.ModelForm):
    class Meta:
        model = models.AddBook
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['name', 'email', 'body']