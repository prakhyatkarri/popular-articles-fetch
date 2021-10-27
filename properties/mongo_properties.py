import json


class MongoProperties:

    def __init__(self):
        try:
            with open('./secrets/mongo.json') as mf:
                self.keys = json.load(mf)
        except Exception as e:
            print('logging exception: %s', e)
