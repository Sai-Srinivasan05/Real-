import json
import boto3

a = boto3.client('comprehend')
b = boto3.client('dynamodb')

c = 'SentimentAnalysisResults'

def lambda_handler(d, e):
    for f in d['Records']:
        g = json.loads(f['kinesis']['data'])
        h = g['text']
        
        i = a.detect_sentiment(
            Text=h,
            LanguageCode='en'
        )
        
        j = i['Sentiment']
        k = i['SentimentScore']
        
        b.put_item(
            TableName=c,
            Item={
                'TweetId': {'S': g['id_str']},
                'Text': {'S': h},
                'Sentiment': {'S': j},
                'SentimentScore': {'M': {
                    'Positive': {'N': str(k['Positive'])},
                    'Negative': {'N': str(k['Negative'])},
                    'Neutral': {'N': str(k['Neutral'])},
                    'Mixed': {'N': str(k['Mixed'])}
                }}
            }
        )
    return {
        'statusCode': 200,
        'body': json.dumps('Sentiment analysis completed')
    }
