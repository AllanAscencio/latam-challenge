from typing import List, Tuple
from datetime import datetime
from collections import defaultdict
import json

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Dictionary to store tweet counts for each date
    date_tweet_count = defaultdict(int)
    
    # Nested dictionary to store user tweet counts per date
    date_user_count = defaultdict(lambda: defaultdict(int))
    
    # Open the file and process it line by line to save memory
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            tweet = json.loads(line)
            
            # Parse the tweet date
            tweet_date = datetime.strptime(tweet['date'], '%Y-%m-%dT%H:%M:%S%z').date()
            
            # Increment the tweet count for the date
            date_tweet_count[tweet_date] += 1
            
            # Increment the tweet count for the user on that date
            username = tweet['user']['username']
            date_user_count[tweet_date][username] += 1

    # Once the file has been processed, find the top 10 dates
    top_10_dates = sorted(date_tweet_count.items(), key=lambda x: x[1], reverse=True)[:10]
    
    # Find the user with the most tweets for each top date
    result = []
    for date, _ in top_10_dates:
        top_user = max(date_user_count[date].items(), key=lambda x: x[1])[0]
        result.append((date, top_user))
    
    # Clear dictionaries to free up memory (memory optimization)
    date_tweet_count.clear()
    date_user_count.clear()

    return result