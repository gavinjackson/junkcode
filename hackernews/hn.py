import requests
from bs4 import BeautifulSoup

def scrape_hacker_news(subject):
    # Send GET request to Hacker News search page
    url = f'https://hn.algolia.com/api/v1/search?query={subject}&tags=story'
    response = requests.get(url)
    data = response.json()

    articles = []
    hits = data['hits']

    # Iterate through each result and extract article details
    for hit in hits:
        title = hit['title']
        url = hit['url']
        points = hit['points']
        comments = hit['num_comments']

        article = {
            'title': title,
            'url': url,
            'points': points,
            'comments': comments
        }
        articles.append(article)

    return articles

# Scrape Hacker News articles with subject "ChatGPT"
articles = scrape_hacker_news('ChatGPT')

# Print the scraped articles
for article in articles:
    print(f"Title: {article['title']}")
    print(f"URL: {article['url']}")
    print(f"Points: {article['points']}")
    print(f"Comments: {article['comments']}")
    print()