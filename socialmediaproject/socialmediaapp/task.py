from celery import shared_task
import requests
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)



# @shared_task
# def post_on_facebook():
#     access_token="EAAI79UnV8gIBO4qYjMPN4m7cZCCDMAqtXXWCdwCaZBRTEUqgNZAJIoZARkmkBkwmLm7hgJBdYEZC93H9iVW8wCUdDlD2bNnmC0SOLZAiXRjIceCEFUPuA52IZBIH6XsplZCCq7g5kWvpzudU40He9E2WdwZBh6gUr0FTSbFEYIsEZBcOyNIUbEQTZBznI1g8iUwUYoFTOnO8GfIpIqobkFHAcGlNZC4ZD"
#     # Facebook GraphQL API endpoint
#     api_url = "https://graph.facebook.com/v19.0/me/feed"

#     # Prepare headers
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {access_token}",
#     }

#     try:
#         # Make the GraphQL request
#         response = requests.post(api_url, headers=headers, json={"message": "pranav are you here"})

#         # Check the HTTP status code for success
#         if response.status_code == 200:
#             return True
#         else:
#             return False
#     except Exception as e:
#         # Log the exception or handle it accordingly
#         print(f"An error occurred: {e}")
#         return False
               
@shared_task
def post_on_facebook(message):
    access_token="EAAI79UnV8gIBO3EAwbNzm8A6MdK5Com5slIdsnyhI9tWPMZBIH1oUksZBRkGlTgp98h8l5vqeNyxQDYsue1ZAt96MxYNGZCGg2No6XkcsbXf6f6P88uZCs40sa1hZAljcw7cq56xPgDZCkpGs9Gso05MaeCfnlEzWGVXzn7UUG6hoZA8oK0v8WIU2JZAnwrhJg0yzBMlmMcXfJVdadTGeJ8YMXbAZD"
    api_url = "https://graph.facebook.com/v19.0/me/feed"
    
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        'access_token': access_token,
        'message': message,
    }


    try:
        # Make the GraphQL request
        response = requests.post(api_url, headers=headers, data=data)
        if response.status_code == 200:
            logger.info("Facebook post successful")
            return True
        else:
            logger.error(f"Facebook post failed: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        logger.exception("An error occurred during Facebook post")
        return False