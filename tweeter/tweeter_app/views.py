from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from tweeter_app.forms import SignupForm, LoginForm, TweetForm
from tweeter_app.models import MyUser, MyTweet
import ipdb

# Create your views here.

def signup(request):
    form = SignupForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = MyUser.objects.create_user(username=form.cleaned_data["username"], password=form.cleaned_data["password"], email=form.cleaned_data["email"])
            if user is not None:
                return render(request, "home.html", {'user': user})
    return render(request, "signup.html", {"form": form})

def home(request):
    form = TweetForm(request.POST or None)
    user = request.user
    tweets = MyTweet.objects.all()
    if request.method == "POST":
        if form.is_valid() and request.user is not None:
            tweet = form.save(commit=False)
            tweet.user = request.user.myuser
            tweet.save()
        else:
            print(form.errors)

    return render(request,"home.html", {'user': user, "form": form, "tweets": tweets})


def login(request):
    form = LoginForm(request.POST or None)

    if request.user.is_authenticated:
        return render(request, "home.html", {'user': request.user, "form": TweetForm()})

    if request.method == "POST":
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return render(request, "home.html", {'user': user, 'form': TweetForm()})
    return render(request, "login.html", {'form': form})
