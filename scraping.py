import requests
from bs4 import BeautifulSoup

def scrape_news_titles(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Print response content for debugging
    print(response.content)
    
    # Check if request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all elements with the specified class (assuming articles have the same class)
        articles = soup.find_all(class_='cd__headline-text')
        
        # Extract and print titles of the articles
        for article in articles:
            print(article.text)
    else:
        print("Failed to retrieve page:", response.status_code)

# URL of the news website you want to scrape
url = 'https://edition.cnn.com/'

# Call the function to scrape news titles
scrape_news_titles(url)
