# Real-Time Twitter Sentiment Analysis Leveraging AWS Services

This project demonstrates how to perform real-time sentiment analysis on Twitter data using AWS cloud services. By utilizing AWS services such as **Lambda**, **Kinesis**, **S3**, **DynamoDB**, and **Comprehend**, the system continuously captures, processes, and analyzes tweets, categorizing them based on sentiment (positive, negative, neutral).

## Table of Contents
- [Architecture Overview](#architecture-overview)
- [AWS Services Used](#aws-services-used)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Architecture Overview

The architecture for real-time Twitter sentiment analysis includes the following steps:
1. **Tweet Streaming**: Twitter API streams real-time tweets based on specified keywords.
2. **AWS Kinesis**: Tweets are ingested into AWS Kinesis Data Stream for real-time processing.
3. **AWS Lambda**: A Lambda function processes the incoming stream of tweets and sends them to AWS Comprehend for sentiment analysis.
4. **AWS Comprehend**: Performs sentiment analysis on the text and classifies it into categories: Positive, Negative, Neutral, or Mixed.
5. **AWS DynamoDB**: Results from sentiment analysis are stored in a DynamoDB table for real-time querying and analytics.
6. **AWS S3**: Tweets and their sentiment classifications are stored in S3 for long-term storage and batch analysis.

## AWS Services Used

- **Amazon Kinesis**: For real-time ingestion of Twitter data streams.
- **AWS Lambda**: Serverless compute to process incoming tweets and trigger the sentiment analysis.
- **Amazon Comprehend**: AWS-managed NLP service for sentiment analysis.
- **Amazon DynamoDB**: NoSQL database to store and query sentiment results.
- **Amazon S3**: Storage service for persisting raw tweets and analyzed data.
- **AWS IAM**: For access control and service permissions.

## Customization

You can customize the following aspects of the project:
- **Sentiment Categories**: Modify how sentiment is classified in the Lambda function.
- **Keyword Filters**: Change the keywords or hashtags being tracked by modifying the Twitter stream query.
- **Data Storage**: Change the way data is stored or retrieved by configuring DynamoDB or S3.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
