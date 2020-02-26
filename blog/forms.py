#to create models forms
from blog.models import Users
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Comment , Reply ,Post


class UserForm(UserCreationForm):

    class Meta:
        fields=('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        model = get_user_model()
        help_texts = {
            'username': None,
            'email': None,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label='User Name'
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['email'].label='Email'
        self.fields['password1'].label='Password'
        self.fields['password2'].label = 'Re-Enter Password'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug','content', 'status','cat','image','id',)
