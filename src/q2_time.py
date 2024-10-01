from typing import List, Tuple
from collections import defaultdict
import re
import ujson as json  # Faster JSON processing
import heapq
import os
from multiprocessing import Pool, cpu_count

# Emoji regex pattern
emoji_pattern = re.compile(
    '['
    u'\U0001F600-\U0001F64F'  # Emoticons
    u'\U0001F300-\U0001F5FF'  # Symbols & Pictographs
    u'\U0001F680-\U0001F6FF'  # Transport & Map
    u'\U0001F1E0-\U0001F1FF'  # Flags
    ']+', flags=re.UNICODE)

# Function to process each line
def process_line_for_emojis(line: str) -> List[Tuple[str, int]]:
    emoji_counts = defaultdict(int)
    try:
        tweet = json.loads(line)
        content = tweet.get('content', '')
        if not isinstance(content, str):
            return []

        # Find all emojis in the tweet content
        emojis = emoji_pattern.findall(content)

        # Count the emojis
        for emoji in emojis:
            emoji_counts[emoji] += 1

    except Exception:
        return []

    # Convert dict_items to a list of tuples before returning
    return list(emoji_counts.items())

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    # Dictionary to store emoji counts
    emoji_count = defaultdict(int)

    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        # Use multiprocessing to parallelize the processing of lines
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Use Pool to distribute the workload across available CPU cores
        with Pool(cpu_count()) as pool:
            results = pool.map(process_line_for_emojis, lines)

        # Combine the results
        for result in results:
            for emoji, count in result:
                emoji_count[emoji] += count

    except Exception as e:
        print(f"Error reading file: {e}")
        return []

    # Use heapq to get the top 10 most used emojis in O(n log k)
    top_10_emojis = heapq.nlargest(10, emoji_count.items(), key=lambda x: x[1])

    return top_10_emojis

if __name__ == "__main__":
    file_path = "tweets.json/farmers-protest-tweets-2021-2-4.json"
    result = q2_time(file_path)
    print(f"q2_time result: {result}")  