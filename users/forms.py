from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200)
    password1 = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        # use get_user_model() instead of settings.AUTH_USER_MODEL here because 
        # https://stackoverflow.com/questions/68988807/django-forms-gives-str-object-has-no-attribute-meta
        model = get_user_model()
        fields = ['email']