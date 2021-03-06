from blog.models import Users, Category
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):

    class Meta:
        fields=('username','first_name','last_name', 'email','password1','password2','is_staff', 'is_active')
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
        self.fields['password1']
        self.fields['password2']
        self.fields['is_staff'].label='Admin'
        self.fields['is_active'].label='Status'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
