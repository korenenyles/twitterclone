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


def profile_view(request, user_id):
    #count of how many users they are following
    #count of how many tweets that user has written
    
    user_tweets = Tweet.objects.filter(author=user_id)
    return render(request, 'profile.html',{'user_tweets':user_tweets})

def follow_user(request, user_id):

    follow_user = TwitterUser.objects.get(id=user_id)
    request.user.following.add(follow_user)
    return HttpResponseRedirect(reverse('profile', kwargs={'user_id':user_id}))
    


def unfollow_user(request, user_id):
    follow_user = TwitterUser.objects.get(id=user_id)
    request.user.following.remove(follow_user)