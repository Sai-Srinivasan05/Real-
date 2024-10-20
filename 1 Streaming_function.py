import json
import tweepy
import boto3

a = 'your_consumer_key'
b = 'your_consumer_secret'
c = 'your_access_token'
d = 'your_access_token_secret'

e = boto3.client('kinesis', region_name='us-east-1')
f = 'twitter-stream'

class G(tweepy.StreamListener):
    def on_data(self, h):
        try:
            i = json.loads(h)

            if 'text' in i:
                j = e.put_record(
                    StreamName=f,
                    Data=json.dumps(i),
                    PartitionKey=i['user']['screen_name']
                )
                print("Tweet sent to Kinesis:", j)
        except Exception as k:
            print(f"Error: {str(k)}")
            return True

    def on_error(self, l):
        print(f"Error: {l}")
        if l == 420:
            return False
        return True

auth = tweepy.OAuthHandler(a, b)
auth.set_access_token(c, d)

m = tweepy.Stream(auth=auth, listener=G())

m.filter(track=["AWS", "cloud", "technology"], languages=["en"])
