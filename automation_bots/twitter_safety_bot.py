# File: twitter_safety_bot.py
import tweepy
import re
import time

# ======== CONFIGURATION ========
BRAND_NAMES = ["YourBrand", "AlternateBrandName"] 
KEYWORDS = ["discount", "offer", "free", "deal"]  # Your trigger words
SAFETY_MSG = "⚠️ Safety Check: Are you sure this is a genuine offer? Verify before sharing personal information."

# Twitter API v2 Credentials (Essential)
BEARER_TOKEN = "your_bearer_token"
CONSUMER_KEY = "your_consumer_key"
CONSUMER_SECRET = "your_consumer_secret"
ACCESS_TOKEN = "your_access_token"
ACCESS_SECRET = "your_access_secret"

# ======== CORE FUNCTIONS ========
class SafetyBot:
    def __init__(self):
        self.client = tweepy.Client(
            bearer_token=BEARER_TOKEN,
            consumer_key=CONSUMER_KEY,
            consumer_secret=CONSUMER_SECRET,
            access_token=ACCESS_TOKEN,
            access_token_secret=ACCESS_SECRET
        )
        self.seen_tweets = set()  # Prevent duplicate actions

    def _contains_trigger(self, text):
        """Detect brand + keyword combinations"""
        text_lower = text.lower()
        brand_pattern = r'\b(' + '|'.join(BRAND_NAMES) + r')\b'
        keyword_pattern = r'\b(' + '|'.join(KEYWORDS) + r')\b'
        
        has_brand = re.search(brand_pattern, text_lower, flags=re.IGNORECASE)
        has_keyword = re.search(keyword_pattern, text_lower)
        return has_brand and has_keyword

    def monitor_and_respond(self):
        """Main execution loop"""
        query = f"({' OR '.join(BRAND_NAMES)}) ({' OR '.join(KEYWORDS)}) -is:retweet"
        
        while True:
            try:
                tweets = self.client.search_recent_tweets(
                    query=query,
                    max_results=10,
                    tweet_fields=["author_id", "conversation_id"]
                )
                
                if not tweets.data:
                    continue

                for tweet in tweets.data:
                    if tweet.id not in self.seen_tweets:
                        if self._contains_trigger(tweet.text):
                            self.client.create_tweet(
                                text=SAFETY_MSG,
                                in_reply_to_tweet_id=tweet.id
                            )
                            self.seen_tweets.add(tweet.id)
                            print(f"Replied to tweet: {tweet.id}")

                time.sleep(300)  # 5-min interval between checks

            except tweepy.TweepyException as e:
                print(f"Error: {str(e)}")
                time.sleep(900)  # Cool-off period

if __name__ == "__main__":
    bot = SafetyBot()
    bot.monitor_and_respond()