import os
import requests
import json

# Fetch the API keys from environment variables
news_api_key = os.getenv("NEWS_API_KEY")

# Tap into NewsAPI
def get_news(topic):
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={news_api_key}&pageSize=5"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            news_json = response.json()

            final_news = []  # List to hold formatted news strings
            for article in news_json["articles"]:
                title_description = f"""
                    Title: {article["title"]},
                    Author: {article["author"]}
                    Source: {article["source"]["name"]}
                    Description: {article["description"]}
                    URL: {article["url"]}
                """
                final_news.append(title_description.strip())

            return final_news
        else:
            print(f"Failed to fetch news, status code: {response.status_code}")
            return []
    except requests.exceptions.RequestException as e:
        print("Error Occurred during API Request!", e)
        return []

def main():
    news = get_news("bitcoin")
    if news:
        print(news[0])
    else:
        print("No news found.")

if __name__ == "__main__":
    main()

