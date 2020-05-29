from django.shortcuts import render, reverse, HttpResponseRedirect

from django.contrib.auth import login, logout, authenticate
from twitteruser.models import TwitterUser
from tweet.models import Tweet

from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def homeView(request):
    html = 'index.html'
    user_data = TwitterUser.objects.all()
    tweet_data = Tweet.objects.all().order_by('-date')
   

    return render(request, html, {"user_data": user_data, 'tweet_data':tweet_data})


def profile_view(request, user_id):
    #count of how many users they are following
    #count of how many tweets that user has written
    #https://stackoverflow.com/questions/3373565/select-a-count-using-django-model
    
    user_tweets = Tweet.objects.filter(author = user_id).order_by('-date')
    twitteruser = TwitterUser.objects.get(id=user_id)
    following_list = twitteruser.following.all()
    following_count = following_list.count()
    tweet_count = user_tweets.count()

    if request.user.is_authenticated:
        current_user_following_list = request.user.following.all()
        if twitteruser in current_user_following_list:
            is_following = True
        else:
            is_following = False
        return render(
                request, 
                'profile.html', {
                'user_tweets': user_tweets, 
                'twitteruser': twitteruser, 
                'is_following': is_following,
                'following_count': following_count,
                'tweet_count': tweet_count,
                'current_user_following_list': current_user_following_list,
                })   
                #Peter Marsh and Derek Barnes assisted with this!  
    return render(
                request, 
                'profile.html', {
                'user_tweets': user_tweets, 
                'twitteruser': twitteruser,
                'following_count': following_count,
                'tweet_count':tweet_count,
                })     

    
@login_required
def follow_user(request, id):
    current_user = request.user
    follow_user = TwitterUser.objects.get(id=id)
    current_user.following.add(follow_user)
    current_user.save()
    return HttpResponseRedirect(reverse('profile', kwargs={'user_id':id,}))
# https://stackoverflow.com/questions/6218175/how-to-implement-followers-following-in-django
@login_required
def unfollow_user(request, id):
    current_user = request.user
    follow_user = TwitterUser.objects.get(id=id)
    current_user.following.remove(follow_user)
    current_user.save()
    return HttpResponseRedirect(reverse('profile', kwargs={'user_id':id,}))
    
    
    


