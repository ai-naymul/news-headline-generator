import requests
import os
from dotenv import load_dotenv
import json
load_dotenv()
import logging
TOPIC = 'bitcoin' #should be in lower case
API_KEY = os.getenv('API_KEY')
API_URL = f'https://newsapi.org/v2/everything?q={TOPIC}&apiKey={API_KEY}'


class FetchArticleHeadlines():
    def __init__(self) -> None:
        pass

    def get_article_headline(self):
        logging.info('Getting the request from api URL')
        try:
            response = requests.get(API_URL)
            if response.status_code == 200:
                result = response.json()
                top_ten_articles = result['articles'][:10] # use the number to set it according to your preference
                articles_data = {}

                # Iterate over the top 10 articles and add their data to the dictionary
                for index, article in enumerate(top_ten_articles, start=1):
                    article_key = f"article_{index}"
                    articles_data[article_key] = {
                        'title': article['title'],
                        'description': article['description']
                        }
                # Print the dictionary to see the result
                all_article_data = json.dumps(articles_data, indent=2)
                return all_article_data
            else:
                logging.info(f'No article found from the {API_KEY}')
                return []
        except:
            logging.error('There has been some issue with the request')

