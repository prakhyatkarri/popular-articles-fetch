from service.mongo_service import MongoDbClient
from service.nytimes_service import NyTimesService
from service.kaka_service import KafkaService

if __name__ == '__main__':
    articles = NyTimesService().get_articles()
    print(f'Fetched {len(articles)} articles')

    staged_articles = MongoDbClient().save_articles_to_stage(articles)

    if len(staged_articles) > 0:
        kafka_service = KafkaService()

        for article in staged_articles:
            kafka_service.publish(article)