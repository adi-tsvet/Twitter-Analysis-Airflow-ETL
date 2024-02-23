#import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

def run_twitter_api():

    # Read the existing CSV file
    existing_tweets_df = pd.read_csv('data/twitter_dataset.csv')

    # Initialize an empty list to store the refined tweets
    refined_tweets_list = []

    # Iterate through each row in the existing DataFrame
    for index, row in existing_tweets_df.iterrows():
        refined_tweet = {
            'Tweet_ID': row['Tweet_ID'],
            'Username': row['Username'],
            'Text': row['Text'],
            'Retweets': row['Retweets'],
            'Likes': row['Likes'],
            'Timestamp': row['Timestamp']
        }
        refined_tweets_list.append(refined_tweet)

    # Create a new DataFrame from the refined tweets list
    refined_tweets_df = pd.DataFrame(refined_tweets_list)

    # Write the refined DataFrame to a new CSV file
    # refined_tweets_df.to_csv('s3://airflow-bucket-dev-aditsvet/refined_tweets.csv')
    # Write the refined DataFrame to a new CSV file on S3
    s3 = s3fs.S3FileSystem()
    with s3.open('s3://airflow-bucket-dev-aditsvet/refined_tweets.csv', 'w') as f:
        refined_tweets_df.to_csv(f, index=False)
