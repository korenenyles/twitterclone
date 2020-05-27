from django.shortcuts import render, reverse, HttpResponseRedirect
from twitteruser.forms import SignUpForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from twitteruser.models import TwitterUser
from tweet.models import Tweet

from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def homeView(request):
    html = 'index.html'
    user_data = TwitterUser.objects.all()
    tweet_data = Tweet.objects.all()

    return render(request, html, {"user_data": user_data, 'tweet_data':tweet_data})


def signUpView(request):
    html = 'signup.html'
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = TwitterUser.objects.create_user(
                username=data['username'],
                password=data['password1'],
                
                )
            new_user.save()
            login(request, new_user)
            return HttpResponseRedirect(reverse('home'))
    form = SignUpForm()
    return render(request, html, {'form': form})

def loginview(request):
    html = 'login.html'
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user= authenticate(request, username = data['username'], password= data['password'])
            if user:
                login(request, user)
                
            return HttpResponseRedirect(
                    request.GET.get('next', reverse('home'))
                )
    form = LoginForm()
    return render(request,'login.html', {'form': form})
    

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def profile_view(request, user_id):
    #count of how many users they are following
    #count of how many tweets that use has written
    #users tweets
    user_tweets = Tweet.objects.filter(author=user_id)
    return render(request, 'profile.html',{'user_tweets':user_tweets})