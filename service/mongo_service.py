from pymongo import MongoClient

from properties.app_config import AppConfig


class MongoDbClient:
    CONNECTION_STRING = 'mongodb://{username}:{password}@{host}:{port}/{db}'
    mongo_client = None
    article_collection = None

    def __init__(self):
        mongo_properties = AppConfig().mongo_properties
        username = mongo_properties['username']
        password = mongo_properties['password']
        host = mongo_properties['host']
        port = mongo_properties['port']
        db = mongo_properties['db']

        client = MongoClient(self.CONNECTION_STRING.format(
            username=username,
            password=password,
            host=host,
            port=port,
            db=db
        ))

        self.mongoClient = client['admin']

    def save_articles_to_stage(self, articles):
        saved_article_ids = []

        if articles is not None and len(articles) > 0:
            self.article_collection = self.mongoClient['article']

            for article in articles:
                inserted_id = self.insert_article_to_stage(article)

                if inserted_id != -1:
                    saved_article_ids.append(inserted_id)

        print(f'Upserted {len(saved_article_ids)} records')

        saved_articles = []

        for article in articles:
            if article['id'] in saved_article_ids:
                saved_articles.append(article)

        return saved_articles

    def insert_article_to_stage(self, article):
        article['_id'] = article['id']
        existing_article = self.article_collection.find_one(article['id'])

        if existing_article is None:
            return self.article_collection.insert_one(article).inserted_id
        else:
            return -1
