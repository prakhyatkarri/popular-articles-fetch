from mongo.mongodb import MongoDbClient
from service.nytimes_service import NyTimesService

if __name__ == '__main__':
    articles = NyTimesService().get_articles()
    print(f'Fetched {len(articles)} articles')
    MongoDbClient().save_articles_to_stage(articles)
