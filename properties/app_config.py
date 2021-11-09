from configparser import ConfigParser


class AppConfig:
    api_properties = {}
    mongo_properties = {}
    kafka_properties = {}

    def __init__(self):
        try:
            config = ConfigParser()
            config.read('secrets/application_properties.ini')
            self.api_properties = dict(config['api'])
            self.mongo_properties = dict(config['mongo'])
            self.kafka_properties = dict(config['kafka'])
        except Exception as e:
            print(f'Cannot read Properties: {e}')
