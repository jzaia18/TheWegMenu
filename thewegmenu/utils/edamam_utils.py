import requests, os, json, sys

DIR = os.path.dirname(__file__) or '.'
APP_ID = json.loads(open(DIR + "/../secrets.JSON").read())['edamam_app_id']
APP_KEY = json.loads(open(DIR + "/../secrets.JSON").read())['edamam_app_key']

headers = {
}

params = {
    "app_id": APP_ID,
    "app_key": APP_KEY,
    "from": 0,
    "to": 100,
    "q": "chicken"
}

if __name__ == '__main__':
    resp = json.loads(requests.get("https://api.edamam.com/search", headers=headers, params=params).content)
    # for item in resp['hits']:

    for item in resp['hits']:
        print(item['recipe']['label'])
