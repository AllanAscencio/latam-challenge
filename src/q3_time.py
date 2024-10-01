from typing import List, Tuple
from collections import defaultdict
import json
import os
from multiprocessing import Pool, cpu_count

# Function to process each line
def process_line_for_mentions(line: str) -> List[Tuple[str, int]]:
    mention_counts = defaultdict(int)
    try:
        tweet = json.loads(line)
        mentioned_users = tweet.get('mentionedUsers', [])
        if mentioned_users is None:
            mentioned_users = []

        # Count the mentioned users
        for user in mentioned_users:
            username = user.get('username', '')
            if username:
                mention_counts[username] += 1

    except Exception:
        return []

    # Convert dict_items to a list for serialization
    return list(mention_counts.items())

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    # Dictionary to store mention counts
    mention_count = defaultdict(int)

    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        # Use multiprocessing to parallelize the processing of lines
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Use Pool to distribute the workload across available CPU cores
        with Pool(cpu_count()) as pool:
            results = pool.map(process_line_for_mentions, lines)

        # Combine the results
        for result in results:
            for username, count in result:
                mention_count[username] += count

    except Exception as e:
        print(f"Error reading file: {e}")
        return []

    # Get the top 10 most mentioned users
    top_10_users = sorted(mention_count.items(), key=lambda x: x[1], reverse=True)[:10]

    return top_10_users

if __name__ == "__main__":
    file_path = "tweets.json/farmers-protest-tweets-2021-2-4.json"
    result = q3_time(file_path)
    print(f"q3_time result: {result}")
