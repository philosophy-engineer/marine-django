from django.forms import ModelForm
from .models import Project


class ProjectCreationForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'image', 'description']
