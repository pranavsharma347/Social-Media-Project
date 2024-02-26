from django.shortcuts import render

# Create your views here.
import requests
from facebook import GraphAPI
from django.http import JsonResponse
from socialmediaapp.task import post_on_facebook
import time




def get_facebook_likes(object_id,access_token):
    
    url=f"https://graph.facebook.com/v19.0/{object_id}/?fields=likes.summary(true)&access_token={access_token}"
    like_response = requests.get(url)
    like_data = like_response.json()    
    if "likes" in like_data:
        # Extract the total count from the "summary" field
        total_count = like_data["likes"]["summary"]["total_count"]
        return total_count
    return 0
    



def get_facebook_posts(request):
    # Get user's feed (posts)
    access_token="EAAI79UnV8gIBO944MF1cCA1FmLO3f0ElxU8kPNTJszYDKJhFKqriPnaXZBjYvjV16bPG4MEtgt4ZABP8JbXhesja4YZCuCZBToT9y2910wzpF51xMXP53nv8MaZBj0gJAkDhdzDn3aQhGyBj1Hin7lUAIbqaMZBh4arYDm9mk90l5BrFK3FI4lZAOAE"
    feed_url = f'https://graph.facebook.com/v13.0/me/posts?fields=object_id,message,full_picture&access_token={access_token}'
    feed_response = requests.get(feed_url)
    feed_data = feed_response.json()

    posts = feed_data.get('data', [])

    # Retrieve comments and likes for each post
    for i in range(len(posts)):
        posts[i]["likes"]=get_facebook_likes(posts[i].get("object_id"),access_token)
        
    extracted_posts = [
        {
            "full_picture": post.get("full_picture", ""),
            "message": post.get("message", ""),
            "likes": post.get("likes", 0),
        }
        for post in posts]
    
    return render(request,"post.html",{"posts":extracted_posts})


def schedule_post_in_facebook(request):
    if request.method == "POST":
        time = request.POST["time"]

        # Schedule the Celery task
        response = post_on_facebook.apply_async(args=["this is pranav page"], eta=time[11:16])

        return render(request, "send_post.html")

    return render(request, "send_post.html")



def facebook_page_analytics(request):
    access_token="EAAI79UnV8gIBO6x1TRIKuoWsLCrbnCZA8xzrlO6fqBhIMKytxwoIrLypooNfOKo7neso34ZCqQqPDDYa0XYO3rDrO23inusX5FnUMVyzhGXJBTxe7RWwni06Hnjy31pQ1cY9faqOcp362ySlmUvkjo8n8mbzTvouH40GuvCfEehqiBZAx9Vd1VpyMziq7Te2ALn0ug3ZB6PL5EZC7LmpnecQZD"
    page_url = f'https://graph.facebook.com/v19.0/194342320439098/insights/post_engaged_users&access_token={access_token}'
    page_response = requests.get(page_url)
    page_data = page_response.json()
    # print("feed_data",feed_data)

    pages = page_data.get('data', [])
    
    return render(request,"facebook_analytics.html",{"pages":pages})
    
    
    
    
    
