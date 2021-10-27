import json

keys = ['1']


class TokenProperties:

    def __init__(self):
        try:
            with open('./secrets/key.json') as kf:
                self.keys = json.load(kf)
        except Exception as e:
            print('logging exception: %s', e)
