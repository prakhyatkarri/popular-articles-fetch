from configparser import ConfigParser


class AppConfig:
    api_properties = {}
    mongo_properties = {}

    def __init__(self):
        try:
            config = ConfigParser()
            config.read('secrets/application_properties.ini')
            self.api_properties = dict(config['api'])
            self.mongo_properties = dict(config['mongo'])
        except Exception as e:
            print(f'Cannot read Properties: {e}')
