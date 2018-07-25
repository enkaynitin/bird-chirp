from django.forms import ModelForm, Form
from django import forms
from .models import Chirp


class ChirpForm(ModelForm):
    class Meta:
        model = Chirp
        fields = ['chirp']


class SearchForm(forms.Form):
    search = forms.CharField(label='Search', max_length=50)
