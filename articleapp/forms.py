from django.forms import ModelForm
from django import forms
from projectapp.models import Project
from .models import Article


class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'editable text-left',
            'style': 'height: auto;'
        }
    ))
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)
    
    class Meta:
        model = Article
        fields = ['title', 'project', 'image', 'content']
