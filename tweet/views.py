from django.shortcuts import render, HttpResponseRedirect, reverse
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from tweet.forms import AddTweet
import re
from notification.models import Notification
from django.contrib.auth.decorators import login_required
from django.views.generic import View

# Create your views here.
@login_required
def add_tweet(request, user_id):
    form = AddTweet()
    tweet_data = Tweet.objects.all().order_by('-date')
    if request.method == "POST":
        form = AddTweet(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            all_user = TwitterUser.objects.all()
            user=TwitterUser.objects.get(id=user_id)
            tweet = Tweet.objects.create(
                tweet =data['tweet'],
                author = user
            )
            #https://stackoverflow.com/questions/7150652/regex-valid-twitter-mention
            find_users = re.findall(r'@(\w+)', data['tweet'])
            # Matthew Perry helped fix my regex too.
            for tagged in find_users:
                   
                #Derek Barnes/Matthew Perry assisted with fixing my mess!  
                 
                Notification.objects.create(
                    notify_user = TwitterUser.objects.get(username=tagged),
                    tweet = tweet,
                )
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'addtweet.html', {'form':form, 'tweet_data': tweet_data})


class TweetView(View):
    def get(self, request, tweet_id):
        tweet = Tweet.objects.get(id=tweet_id)
        return render(request, 'tweet.html', {'tweet':tweet})
