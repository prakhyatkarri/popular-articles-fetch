from pymongo import MongoClient

from properties.app_config import AppConfig


class MongoDbClient:
    CONNECTION_STRING = 'mongodb://{username}:{password}@{cluster_name}:27017/{db}'
    mongo_client = None

    def __init__(self):
        mongo_properties = AppConfig().mongo_properties
        username = mongo_properties['username']
        password = mongo_properties['password']
        cluster_name = mongo_properties['host']
        db = mongo_properties['db']

        client = MongoClient(self.CONNECTION_STRING.format(
            username=username,
            password=password,
            cluster_name=cluster_name,
            db=db
        ))

        self.mongoClient = client['admin']

    def save_articles_to_stage(self, articles):
        if articles is not None and len(articles) > 0:
            article_collection = self.mongoClient['article']

            for article in articles:
                self.insert_article_to_stage(article, article_collection)

        print(f'Upserted {len(articles)} records')

    def insert_article_to_stage(self, article, article_collection):
        article['_id'] = article['id']
        existing_article = article_collection.find_one(article['id'])

        if existing_article is None:
            article_collection.insert_one(article)
