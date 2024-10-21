import boto3
import json
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
from configparser import SafeConfigParser

a = SafeConfigParser()
a.read('api_auth.cfg')

b = a.get('api_tracker', 'access_token')
c = a.get('api_tracker', 'access_token_secret')
d = a.get('api_tracker', 'consumer_key')
e = a.get('api_tracker', 'consumer_secret')
f = a.get('api_tracker', 'aws_key_id')
g = a.get('api_tracker', 'aws_key')

h = 'twitter-stream'

i = boto3.client('firehose', region_name='eu-west-1',
                      aws_access_key_id=f,
                      aws_secret_access_key=g)

class J(StreamListener):
    def on_data(self, k):
        l = json.loads(k)
        sentiment_data = {
            'id': l.get('id_str'),
            'text': l.get('text'),
            'user': l.get('user', {}).get('screen_name'),
            'sentiment': '',  # Add sentiment from AWS Comprehend here
            'timestamp': l.get('created_at')
        }
        i.put_record(
            DeliveryStreamName=h,
            Record={'Data': json.dumps(sentiment_data)}  
        )
        print(sentiment_data)
        return True

    def on_error(self, m):
        print(m)

if __name__ == '__main__':
    n = J()
    o = OAuthHandler(d, e)
    o.set_access_token(b, c)
    p = Stream(o, n)

    p.filter(track=['AWS'])
