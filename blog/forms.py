from django import forms
from .models import Post, BlogGroup


class NewPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['group', 'title', 'text', 'image', 'file', 'status', ]


class NewBlogGroupForm(forms.ModelForm):

    class Meta:
        model = BlogGroup
        fields = ['title', ]

