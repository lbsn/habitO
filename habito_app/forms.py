from django import forms
from django.contrib.auth.models import User
from habito_app.models import Habit
from datetime import date
import json

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class HabitForm(forms.ModelForm):

    title = forms.CharField(max_length=128, help_text="Please enter the habit name.")
    description = forms.CharField(max_length=128, help_text="Please write a description.")
    created = forms.DateField(widget=forms.HiddenInput(), initial=date.today)
    days = forms.CharField(widget=forms.HiddenInput(), max_length=128, initial={})
    achv_default = {'1':0,'2':0,'3':0}
    achievements = forms.CharField(widget=forms.HiddenInput(), max_length=128, initial=json.dumps(achv_default))
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Habit
        fields = ('title','description',)
