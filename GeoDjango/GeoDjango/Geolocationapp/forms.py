from django import forms

from .models import Search

class Search_Location_Form(forms.ModelForm):
    class Meta:
        model = Search
        fields = ['address']