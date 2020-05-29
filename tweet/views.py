from django.shortcuts import render, HttpResponseRedirect, reverse
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from tweet.forms import AddTweet
import re
from notification.models import Notification
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_tweet(request, user_id):
    form = AddTweet()
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
            find_users = re.findall(r'@([\w\-])', data['tweet'])
            for find_users in set(all_user):
                #Derek Barnes assisted with fixing my mess!         
                Notification.objects.create(
                    notify_user = TwitterUser.objects.get(username=find_users),
                    tweet = tweet,
                    
                            )
                        

            

        return HttpResponseRedirect(reverse('home'))
    return render(request, 'addtweet.html', {'form':form})

def tweet_view(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    return render(request, 'tweet.html', {'tweet':tweet})