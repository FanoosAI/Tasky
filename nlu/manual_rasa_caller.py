import requests
import json


def call_rasa_nlu(bot_instance, message):
    url = bot_instance.config["parsers"]["rasanlu"]['url'] + '/model/parse'

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    data = json.dumps({"text": message})
    response = requests.post(url, data=data, headers=headers)
    return response.json()
