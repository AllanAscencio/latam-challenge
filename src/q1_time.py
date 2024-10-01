from typing import List, Tuple
from datetime import datetime
from collections import defaultdict
import json
import os

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    date_tweet_count = defaultdict(int)
    date_user_count = defaultdict(lambda: defaultdict(int))

    try:
        # Open and process the file line by line
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    tweet = json.loads(line)
                    tweet_date = datetime.strptime(tweet.get('date', ''), '%Y-%m-%dT%H:%M:%S%z').date()
                    username = tweet['user']['username']
                    
                    # Increment counts
                    date_tweet_count[tweet_date] += 1
                    date_user_count[tweet_date][username] += 1
                except (KeyError, ValueError) as e:
                    print(f"Error parsing tweet: {e}")
                    continue  # Skip the tweet with parsing errors

    except Exception as e:
        print(f"Error reading file: {e}")
        return []

    # Find the top 10 dates with the most tweets
    top_10_dates = sorted(date_tweet_count.items(), key=lambda x: x[1], reverse=True)[:10]

    result = []
    for date, _ in top_10_dates:
        top_user = max(date_user_count[date].items(), key=lambda x: x[1])[0]
        result.append((date, top_user))

    return result
