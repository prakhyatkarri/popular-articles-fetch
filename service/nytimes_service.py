import requests

from properties.app_config import AppConfig


class NyTimesService:
    api_properties = {}

    def __init__(self):
        self.api_properties = AppConfig().api_properties

    def get_articles(self):
        try:
            key = self.api_properties['key']
            popular_articles_url = self.api_properties['url'].format(key=key)
            response = requests.get(popular_articles_url)

            if response.status_code == 200:
                response_json = response.json()
                return response_json['results']
            else:
                return []
        except Exception as e:
            print(f'Exception in API call {e}')
        return []
