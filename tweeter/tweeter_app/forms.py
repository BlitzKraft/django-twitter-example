from django import forms
from tweeter_app.models import MyUser, MyTweet


class SignupForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', 'password', 'email']
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

class TweetForm(forms.ModelForm):
    class Meta:
        model = MyTweet
        fields = ["tweet",]
