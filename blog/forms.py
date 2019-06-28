from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    CATEGORY_CHOICES = [
            ('public', 'public'),
            ('private', 'private'),
            ]
    category = forms.ChoiceField(choices = CATEGORY_CHOICES)
    
    class Meta:
        model = Post
        fields = ['title', 'body', 'category', 'image', ]

        
