from pymongo import MongoClient

from properties.mongo_properties import MongoProperties


class MongoDbClient:
    db_name = ''
    CONNECTION_STRING = 'mongodb://{username}:{password}@{cluster_name}:27017/{db}'
    mongo_client = None

    def __init__(self):
        mongo_properties = MongoProperties().keys
        username = mongo_properties['username']
        password = mongo_properties['password']
        cluster_name = mongo_properties['cluster_name']
        db = mongo_properties['db']

        client = MongoClient(self.CONNECTION_STRING.format(
            username=username,
            password=password,
            cluster_name=cluster_name,
            db=db
        ))

        self.mongoClient = client['admin']
