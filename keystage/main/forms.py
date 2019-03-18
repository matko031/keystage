from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser,student_profile, company_profile



class register_user_form(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'address', 'phone')
        help_texts = {'username': " "}

    password = forms.CharField(widget=forms.PasswordInput)

class register_student_form(forms.ModelForm):

    class Meta:
        model = student_profile
        fields = ('first_name', 'last_name', 'faculty','study_year')

class register_company_form(forms.ModelForm):

    class Meta:
        model = company_profile
        fields = ('name', 'sector')



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
        #fields = [str(field.name) for field in list(CustomUser._meta.get_fields())]
        #fields = ['type']

class account_form(forms.ModelForm):

    #file = forms.FileField(required=False)

    class Meta:
        model = student_profile
        #fields = [str(field.name) for field in list(student_profile._meta.get_fields())]
        #fields.remove('student')
        fields = ['interests']


