import json


class Encoder(json.JSONEncoder):
    def default(self, o):
        if hasattr(o, 'reprJSON'):
            return o.reprJSON()
        return json.JSONEncoder.default(self, o)
