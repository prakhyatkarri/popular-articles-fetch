import requests

from mongo.mongodb import MongoDbClient
from properties.token_properties import TokenProperties


def get_articles():
    try:
        token_properties = TokenProperties()
        key = token_properties.keys['key']
        popular_articles_url = f'https://api.nytimes.com/svc/mostpopular/v2/emailed/7.json?api-key={key}'
        response = requests.get(popular_articles_url)

        if response.status_code == 200:
            response_json = response.json()
            return response_json['results']
        else:
            return []
    except Exception as e:
        print(f'Exception in API call {e}')
    return []


def save_articles(articles):
    if articles is not None and len(articles) > 0:
        article_collection = MongoDbClient().mongoClient['article']

        for article in articles:
            insert_article(article, article_collection)

    print(f'Upserted {len(articles)} records')


def insert_article(article, article_collection):
    article['_id'] = article['id']
    existing_article = article_collection.find_one(article['id'])

    if existing_article is None:
        article_collection.insert_one(article)


if __name__ == '__main__':
    articles = get_articles()
    print(f'Fetched {len(articles)} articles')
    save_articles(articles)
