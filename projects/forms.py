from django import forms
from . import models
from django.utils.translation import gettext as _
attrs = {'class': 'form-control'}


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['Category','title', 'description']
        labels = {
            'Category':_('Category'),
            'title':_('title'),
            'description':_('description'),
        }
        widgets = {
            'Category' : forms.Select(attrs=attrs),
            'title' : forms.TextInput(attrs=attrs),
            'description' : forms.Textarea(attrs=attrs)
       }


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['Category','title', 'status']
        widgets = {
            'Category' : forms.Select(attrs=attrs),
            'title' : forms.TextInput(attrs=attrs),
            'status' : forms.Select(attrs=attrs)
       }
