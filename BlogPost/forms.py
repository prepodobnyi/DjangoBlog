from django import forms
from .models import Posts

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title','text']
        label = {'title':'title','text':'text'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}