import configparser
import tweepy
import pandas as pd
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#vader_lexicon is a list of words with pre defines sentiment scores
nltk.download("vader_lexicon") 

config = configparser.ConfigParser(interpolation=None)

config.read("C:/Users/Dheepansh/Documents/python_tutorial/config.ini")

bearer_token=config["TwitterAPI"]["bearer_token"]

#initialize token
client=tweepy.Client(bearer_token=bearer_token)

#sentiment analyzer
analyzer=SentimentIntensityAnalyzer()

#now clean the imported text
def clean_text(text):
    #removes urls,ats,hashtags,specialcharacters
    text=re.sub(r"http\S+|@\w+|#|[^\w\s]", "",text)
    return text.lower().strip()

#now fetch tweets
def fetch_tweets(query="#tata lang:en -is:retweet", max_results=50):
        #calls recenttweets from twitter 
        response = client.search_recent_tweets(query=query, max_results=max_results, tweet_fields=['id', 'created_at', 'author_id'])
        tweet_data=[]

        if response.data:
              for tweet in response.data:
                    cleaned=clean_text(tweet.text)
                    #the below line uses vader to get scores between -1 to +1
                    score=analyzer.polarity_scores(cleaned)['compound']
                    #labeling the sentiment according to the score
                    label='positive' if score >0 else('negative' if score<0 else 'neutral')

                    tweet_data.append([
                    tweet.id,
                    tweet.text,
                    tweet.created_at,
                    tweet.author_id,
                    score,
                    label
                            ])
        return pd.DataFrame(tweet_data, columns=["tweet_id", "tweet_text", "created_at", "author_id", "sentiment_score", "sentiment_label"])






