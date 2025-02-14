from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Message

class SignUpForm(UserCreationForm):
    class_grade = forms.ChoiceField(choices=User.CLASS_GRADES)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'class_grade')

class LoginForm(AuthenticationForm):
    class_grade = forms.ChoiceField(choices=User.CLASS_GRADES, required=False)

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']