from django import forms
from django.forms import ModelForm

from todo.models import TO_DO


class todoForm(ModelForm):
    class Meta:
        model = TO_DO
        fields = '__all__'


# class ToDoform(forms.Form):
    # text = forms.CharField(max_length=50, label='',
        # widget=forms.TextInput(attrs={'class': 'auto', 'placeholder': 'Write your Plan', }))
