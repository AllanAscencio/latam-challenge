import json
from typing import List, Tuple

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    # Dictionary to store mention counts
    mention_count = {}

    # Process the file line by line and update the in-memory dictionary
    with open(file_path, 'r', encoding='utf-8') as f:
        line_count = 0
        for line in f:
            tweet = json.loads(line)
            mentioned_users = tweet.get('mentionedUsers', [])
            if mentioned_users is None:
                mentioned_users = []

            for user in mentioned_users:
                username = user.get('username', '')
                if username:
                    mention_count[username] = mention_count.get(username, 0) + 1

            line_count += 1
            if line_count % 1000 == 0:
                print(f"Processed {line_count} lines")

    # Get the top 10 most mentioned users
    top_10_users = sorted(mention_count.items(), key=lambda x: x[1], reverse=True)[:10]

    return top_10_users

if __name__ == "__main__":
    file_path = "tweets.json/farmers-protest-tweets-2021-2-4.json"
    result = q3_memory(file_path)
    print(f"q3_memory result: {result}")
