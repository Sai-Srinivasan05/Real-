import json
import boto3

a = boto3.client('comprehend')
b = boto3.client('dynamodb')
sns_client = boto3.client('sns')

c = 'SentimentAnalysisResults'
sns_topic_arn = 'arn:aws:sns:us-east-1:123456789012:HighNegativeSentimentTopic'

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
        
        if k['Negative'] > 0.7:
            sns_client.publish(
                TopicArn=sns_topic_arn,
                Message=f"High negative sentiment detected for tweet: {h}",
                Subject="Negative Sentiment Alert"
            )
            
    return {
        'statusCode': 200,
        'body': json.dumps('Sentiment analysis completed with alert check')
    }
