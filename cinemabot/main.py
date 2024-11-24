

import tweepy
from PIL import Image

# Twitter API credentials
API_KEY = (not leaking)
API_SECRET_KEY = (not leaking)
ACCESS_TOKEN = (not leaking)
ACCESS_TOKEN_SECRET = (not leaking)

# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Function to check mentions and reply with an image
def check_mentions():
    # Get mentions
    mentions = api.mentions_timeline(count=1)  # Only get the most recent mention
    
    for mention in mentions:
        tweet_id = mention.id_str
        username = mention.user.screen_name
        
        # Check if the mention is a reply to the bot
        if username == 'cinema_bot_':
            image_path = 'absolutecinema.jpeg'  # Replace with the path to your image
            
            try:
                # Open the image
                image = Image.open(image_path)
                
                # Upload image
                media = api.media_upload(image_path)
                
                # Post reply with image
                api.update_status(status=':D', media_ids=[media.media_id], in_reply_to_status_id=tweet_id, auto_populate_reply_metadata=True)
                
                # Like the tweet
                api.create_favorite(tweet_id)
                
                print(f'Replied to {username} with image and liked the tweet.')
            except Exception as e:
                print(f'Error: {e}')

# Run the function to check mentions
check_mentions()
