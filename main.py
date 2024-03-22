import os
#from dotenv import load_dotenv
import openai
import requests
import json
import time
import logging
from datetime import datetime
import streamlit as st

# Fetch the OpenAI API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')
#api_key="osenviron.get("NEWS_API_KEY")

# Fetch New_API_Key
news_api_key = os.getenv("NEWS_API_KEY")
#news_api_key=osenviron.get("NEWS_API_KEY")

client = openai.OpenAI()
model = "gpt-3.5-turbo=16k"

# Tap into NewsAPI
def get_news(topic):
    url = (
        f"https://newsapi.org/v2/everything?q={topic}&apiKey={news_api_key}&pageSize=5"
    )

    try:
        response = requests.get(url)
        if response.status_code == 200:
            news = json.dumps(response.json(), indent=4)
            news_json = json.loads(news)

            data = news_json

            # Access all the fields == loop
            status = data["status"]
            total_results = data["totalResults"]
            articles = data["articles"]

            final_news = [] # Pass to: final_news.append(title_description)


            # Loop through articles
            for article in articles:
                source_name = article["source"]["name"]
                author = article["author"]
                title = article["title"]
                description = article["description"]
                url = article["url"]
                content = article ["content"]
                # Put above in a string
                title_description = f"""
                    Title: {title},
                    Author: {author}
                    Source: {source_name}
                    Description: {description}
                    URL: {url}
                """
                final_news.append(title_description)


            return final_news
        else:
            return []


    except requests.exceptions.RequestException as e:
        print("Error Occured during API Request!", e)


def main():
   news = get_news("bitcoin") 
   print(news[0])

if __name__ == "__main__":
    main()
