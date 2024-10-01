from typing import List, Tuple
import json
from collections import defaultdict
import re

# Emoji regex pattern
emoji_pattern = re.compile(
    '['
    u'\U0001F600-\U0001F64F'  # Emoticons
    u'\U0001F300-\U0001F5FF'  # Symbols & Pictographs
    u'\U0001F680-\U0001F6FF'  # Transport & Map
    u'\U0001F1E0-\U0001F1FF'  # Flags
    ']+', flags=re.UNICODE)

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    emoji_count = defaultdict(int)
    
    # Open file and process line by line to save memory
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            tweet = json.loads(line)
            content = tweet['content']
            
            # Find all emojis in the tweet content
            emojis = emoji_pattern.findall(content)
            
            # Increment the emoji counts
            for emoji in emojis:
                emoji_count[emoji] += 1

    # Get the top 10 most used emojis
    top_10_emojis = sorted(emoji_count.items(), key=lambda x: x[1], reverse=True)[:10]

    return top_10_emojis
