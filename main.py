import os
#from dotenv import load_dotenv
import openai
import requests
import json
import time
import logging
from datetime import datetime
import streamlit as st

# fetch the openai api key from environment variables
api_key = os.getenv('openai_api_key')
#api_key="osenviron.get("news_api_key")

# fetch new_api_key
news_api_key = os.getenv("news_api_key")
#news_api_key=osenviron.get("news_api_key")

client = openai.openai()
model = "gpt-3.5-turbo=16k"

# tap into newsapi
def get_news(topic):
    url = (
        f"https://newsapi.org/v2/everything?q={topic}&apikey={news_api_key}&pagesize=5"
    )

    try:
        response = requests.get(url)
        if response.status_code == 200:
            news = json.dumps(response.json(), indent=4)
            news_json = json.loads(news)

            data = news_json

            # access all the fields == loop
            status = data["status"]
            total_results = data["totalresults"]
            articles = data["articles"]

            final_news = [] # pass to: final_news.append(title_description)


            # loop through articles
            for article in articles:
                source_name = article["source"]["name"]
                author = article["author"]
                title = article["title"]
                description = article["description"]
                url = article["url"]
                content = article ["content"]
                # put above in a string
                title_description = f"""
                    title: {title},
                    author: {author}
                    source: {source_name}
                    description: {description}
                    url: {url}
                """
                final_news.append(title_description)


            return final_news
        else:
            return []


    except requests.exceptions.RequestException as e:
        print("Error Occured during API Request!", e)


def main():
   news = get_news("bitcoin") 
   print(news[2])

# Create Class 
class AssistantManager:
    thread_id = None
    assistant_id = None

    """
    - This code defines the constructor method `__init__` for a class
    - `self` refers to the instance of the class being created and is how
    the object can refer to itself.
    - `model` a global variable which is defined above with the value GPT
    """
    def __init__(self, model: str = model) -> None:
        self.client = client
        self.model = model
        self.assistant = None
        self.thread = None
        self.run = None
        self.summary = None

        if AssistantManager.assistant_id:
            self.assistant = self.client.beta.assistants.retieve(
                assistant_id=AssistantManager.assistant_id
            )

        if AssistantManager.thread_id:
            self.thread_id = self.client.beta.threads.retrieve(
                thread_id=AssistantManager.thread_id
            )
        


if __name__ == "__main__":
    main()
