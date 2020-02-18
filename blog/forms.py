#to create models forms
from blog.models import User
from django import forms

class UserForm(forms.ModelForm):
    #to customize how the form look on the web page
    firstName = forms.CharField(label='First Name*')
    lastName= forms.CharField(label='Last Name*')
    email = forms.EmailField(label='Email*')
    password = forms.CharField(label= 'Password', widget=forms.PasswordInput(), min_length=8)
    checkPassword = forms.CharField(label= 'Re-enter Password', widget=forms.PasswordInput(), min_length=8)

    #form validation
    class Meta:
        model= User
        fields= ('firstName','lastName','email','password','checkPassword')

    def validatePassword(self):
        cleanData= self.clean_data #to check if data is valid

        if cleanData['password'] != cleanData['checkPassword']:
            raise forms.ValidationError("password didn't match")

        return cleanData['checkPassword']


    def validateName(self):
        cleanData= self.cleaned_data

        if User.objects.filter(firstName=cleanData['firstName']).exists():
            raise forms.ValidationError("repeated name")

        return cleanData['firstName']


