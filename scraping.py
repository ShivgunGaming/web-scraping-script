import requests
from bs4 import BeautifulSoup

def scrape_news_titles(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url, timeout=10)  # Added a timeout to handle slow responses
        
        # Log response content for debugging
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Headers: {response.headers}")
        
        # Check if request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all elements with the specified class (assuming articles have the same class)
            articles = soup.find_all(class_='cd__headline-text')

            # Check if articles were found, else log a message
            if articles:
                # Extract and print titles of the articles
                for idx, article in enumerate(articles, start=1):
                    print(f"{idx}. {article.text}")
            else:
                print("No articles found with the specified class.")
        else:
            print(f"Failed to retrieve page. Status code: {response.status_code}")

    except requests.Timeout:
        print("The request timed out. Try again later.")
    except requests.ConnectionError:
        print("Failed to connect to the server. Please check your network.")
    except Exception as e:
        print(f"An error occurred: {e}")

# URL of the news website you want to scrape
url = 'https://example.com'

# Call the function to scrape news titles
scrape_news_titles(url)
