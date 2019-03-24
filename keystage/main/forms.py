from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser,student_profile, company_profile, company_internships



class register_user_form(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')
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


class add_internship_form(forms.ModelForm):

    class Meta:
        model = company_internships
        fields = ['name', 'target_faculty']


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        #fields = UserChangeForm.Meta.fields
        fields = ['phone']

class account_form(forms.ModelForm):

    #file = forms.FileField(required=False)

    class Meta:
        model = student_profile
        fields = [str(field.name) for field in list(student_profile._meta.get_fields())]
        fields.remove('student')


