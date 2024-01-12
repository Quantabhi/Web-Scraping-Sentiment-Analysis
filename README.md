# Sentiment Analysis on Financial News

This Python script performs sentiment analysis on financial news articles from specified URLs using web scraping, sentiment analysis, and data visualization libraries.

## Usage

1. **Modify the URLs List:** Edit the `urls` list in the script (`your_script_name.py`) to include the URLs of financial news pages you want to analyze.

    ```python
    # Example URLs
    urls = [
        'https://www.financialexpress.com/market/',
        'https://economictimes.indiatimes.com/markets/stocks/news',
        'https://www.moneycontrol.com/news/business/markets/'
        # Add more URLs as needed
    ]
    ```

2. **Run the Script:** Execute the script to gather data and perform sentiment analysis.

    ```bash
    # Run the script
    python your_script_name.py
    ```

3. **View Results:** After running the script, view the overall sentiment and a scatter plot showing sentiment polarity vs. subjectivity.

## How It Works

The script follows these steps:

- **HTTP Requests:** Makes HTTP requests to specified URLs using the `requests` library.
- **Text Extraction:** Extracts text content from 'h2', 'li', and 'div' tags using BeautifulSoup (`bs4`).
- **Sentiment Analysis:** Performs sentiment analysis on the extracted text using TextBlob.
- **Data Storage:** Creates a Pandas DataFrame to store the results.
- **Overall Sentiment:** Calculates the overall sentiment of all articles.
- **Display:** Shows the overall sentiment.
- **Data Visualization:** Plots a scatter plot using Seaborn to visualize sentiment polarity vs. subjectivity.

## Results

The script generates a Pandas DataFrame with columns 'Text', 'Sentiment Polarity', and 'Sentiment Subjectivity'. Additionally, it displays the overall sentiment and a scatter plot for a visual representation of sentiment analysis.

##Requirements
pip install requests beautifulsoup4 textblob pandas seaborn
##Disclaimer
This script is intended for educational purposes only. Use responsibly and ensure compliance with the terms of service of the websites you are scraping.
