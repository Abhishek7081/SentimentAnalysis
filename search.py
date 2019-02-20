import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
name = input("Input your search query or any person name !!! ")
type(name)
public_tweets = api.search(name)


for tweet in public_tweets:
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    # print(analysis.sentiment)
    if analysis.sentiment.polarity>=0:
    	print("Positive Tweet")
    elif analysis.sentiment.polarity==0:
    	print("Neutral Tweet")
    else:
    	print("Negative Tweet")
    print("")
