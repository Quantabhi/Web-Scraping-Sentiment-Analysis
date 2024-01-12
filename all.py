# Import necessary libraries
import requests  # For making HTTP requests
from bs4 import BeautifulSoup  # For parsing HTML
from textblob import TextBlob  # For sentiment analysis
import pandas as pd  # For data manipulation
import seaborn as sns  # For statistical data visualization
import matplotlib.pyplot as plt  # For creating plots

# List of URLs
urls = [
    'https://www.financialexpress.com/market/',
    'https://economictimes.indiatimes.com/markets/stocks/news',
    'https://www.moneycontrol.com/news/business/markets/'
    # Add more URLs as needed
]

# Define Headers to simulate a request from a web browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

# Create empty lists to store data
texts = []
sentiment_polarities = []
sentiment_subjectivities = []

# Iterate over the list of URLs
for url in urls:
    # Make an HTTP Request to the specified URL with the defined headers
    response = requests.get(url, headers=headers)
    html_content = response.text

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find text content for 'a' tags
    anchor_tags = soup.find_all('li', class_='clearfix')
    for li_tag in anchor_tags:
        # Extract text content from 'h2' tags
        h2_tags = li_tag.find_all('h2')
        text_content = ' '.join([h2.text for h2 in h2_tags])

        # Perform Sentiment Analysis using TextBlob
        analysis = TextBlob(text_content)

        # Append data to lists
        texts.append(text_content)
        sentiment_polarities.append(analysis.sentiment.polarity)
        sentiment_subjectivities.append(analysis.sentiment.subjectivity)

    # Find text content for 'h2' tags
    h2_tags = soup.find_all('h2', class_='entry-title')
    for tag in h2_tags:
        # Perform Sentiment Analysis using TextBlob
        analysis = TextBlob(tag.text)

        # Append data to lists
        texts.append(tag.text)
        sentiment_polarities.append(analysis.sentiment.polarity)
        sentiment_subjectivities.append(analysis.sentiment.subjectivity)

    # Find text content for 'div' tags
    div_tags = soup.find_all('div', class_='eachStory')
    for tag in div_tags:
        # Perform Sentiment Analysis using TextBlob
        analysis = TextBlob(tag.text)

        # Append data to lists
        texts.append(tag.text)
        sentiment_polarities.append(analysis.sentiment.polarity)
        sentiment_subjectivities.append(analysis.sentiment.subjectivity)

# Create a DataFrame
data = {'Text': texts, 'Sentiment Polarity': sentiment_polarities, 'Sentiment Subjectivity': sentiment_subjectivities}
df = pd.DataFrame(data)

# Calculate overall sentiment
overall_sentiment = TextBlob(' '.join(texts)).sentiment

# Display the overall sentiment
print(f"Overall Sentiment - Polarity: {overall_sentiment.polarity}, Subjectivity: {overall_sentiment.subjectivity}")

# Plot the data using Seaborn
sns.scatterplot(x='Sentiment Polarity', y='Sentiment Subjectivity', data=df)
plt.title('Sentiment Analysis')
plt.show()