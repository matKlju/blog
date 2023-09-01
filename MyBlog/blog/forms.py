from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class PostSearchForm(forms.Form):
    query = forms.CharField(label='Search by Title', max_length=100)