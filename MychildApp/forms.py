from django import forms
from .models import Activities, Posts 

class ActivitiesForm(forms.ModelForm):
    class Meta:
        model = Activities
        fields = ['name', 'description', 'requirements', 'file']
class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['file', 'description']