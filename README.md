# Real-Time Twitter Sentiment Analysis Leveraging AWS Services

This project demonstrates how to perform real-time sentiment analysis on Twitter data using AWS cloud services. By utilizing AWS services such as **Lambda**, **Kinesis**, **S3**, **DynamoDB**, and **Comprehend**, the system continuously captures, processes, and analyzes tweets, categorizing them based on sentiment (positive, negative, neutral).

## Table of Contents
- [Architecture Overview](#architecture-overview)
- [AWS Services Used](#aws-services-used)
- [Setup and Prerequisites](#setup-and-prerequisites)
- [Installation](#installation)
- [Running the Project](#running-the-project)
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
7. **Dashboard/Visualization**: Optional setup for visualizing sentiment trends in real time using services like Amazon QuickSight or external visualization tools.

## AWS Services Used

- **Amazon Kinesis**: For real-time ingestion of Twitter data streams.
- **AWS Lambda**: Serverless compute to process incoming tweets and trigger the sentiment analysis.
- **Amazon Comprehend**: AWS-managed NLP service for sentiment analysis.
- **Amazon DynamoDB**: NoSQL database to store and query sentiment results.
- **Amazon S3**: Storage service for persisting raw tweets and analyzed data.
- **AWS IAM**: For access control and service permissions.

## Setup and Prerequisites

### Prerequisites:
- An **AWS Account**.
- Basic knowledge of AWS services (IAM, Lambda, Kinesis, S3, DynamoDB, Comprehend).
- Python 3.x installed on your local machine.
- **Twitter API credentials** to access the Twitter stream.

### AWS IAM Permissions:
Ensure that you have appropriate permissions to create and manage AWS resources like Lambda functions, Kinesis streams, and DynamoDB tables.

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Real-Time-Twitter-Sentiment-Analysis.git
cd Real-Time-Twitter-Sentiment-Analysis
```

### 2. Install Dependencies
Make sure you have the required Python libraries installed:
```bash
pip install -r requirements.txt
```

### 3. Set Up AWS Credentials
Ensure your AWS credentials are correctly configured in your environment. You can use the `aws configure` command to set them up:
```bash
aws configure
```

### 4. Set Up Twitter API Credentials
Create a `.env` file and add your Twitter API keys:
```bash
TWITTER_API_KEY=your_api_key
TWITTER_API_SECRET=your_api_secret
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_SECRET=your_access_secret
```

## Running the Project

### 1. Deploy AWS Infrastructure
Use AWS CLI or the AWS Management Console to set up the necessary services:
- Create a Kinesis Data Stream.
- Set up a DynamoDB table.
- Create an S3 bucket for storing data.
- Deploy a Lambda function to process the stream.

### 2. Run the Twitter Stream Listener
Run the Python script that connects to the Twitter API and sends data to the Kinesis stream:
```bash
python stream_twitter.py
```

### 3. Monitor Real-Time Sentiment
The Lambda function will automatically trigger when data arrives in the Kinesis stream. You can monitor real-time sentiment results in DynamoDB, or use AWS S3 to collect and analyze data in bulk.

### Optional: Set Up Dashboard for Visualization
If you'd like to visualize sentiment trends in real-time, you can connect your DynamoDB data to **Amazon QuickSight** or use other tools like Grafana or Kibana.

## Customization

You can customize the following aspects of the project:
- **Sentiment Categories**: Modify how sentiment is classified in the Lambda function.
- **Keyword Filters**: Change the keywords or hashtags being tracked by modifying the Twitter stream query.
- **Data Storage**: Change the way data is stored or retrieved by configuring DynamoDB or S3.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
