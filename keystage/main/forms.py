from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser,student_profile

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('type','address')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
        #fields = [str(field.name) for field in list(CustomUser._meta.get_fields())]
        #fields = ['type']

class student_profile_form(forms.ModelForm):

    class Meta:
        model = student_profile
        fields = [str(field.name) for field in list(student_profile._meta.get_fields())]

