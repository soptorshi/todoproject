from django import forms
from todoApp.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'name',
            'desc'
        ]

# class TaskForm(forms.Form):
#     name = forms.CharField(max_length=20, required=False,
#              widget= forms.TextInput(attrs = {
#                 'reruired': 'True'
#              }))
#     desc = forms.CharField(max_length=60, required=False,
#     widget= forms.TextInput(attrs = {
#             'required':'True'
#         }))