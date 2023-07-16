from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label='Your Email')
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.Form):
    name = forms.CharField(max_length=255, label='Your Name')
    email = forms.EmailField(label='Your Email')
    user_type = forms.ChoiceField(choices=[('investor', 'Investor'), ('innovator', 'Innovator')], label='Select User Type')
    password = forms.CharField(widget=forms.PasswordInput)

from .models import Idea

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['idea_name', 'author', 'idea_subject', 'idea_description', 'amount_expecting']