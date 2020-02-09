import requests, os, json, sys, mongo_utils

DIR = os.path.dirname(__file__) or '.'
APP_ID = json.loads(open(DIR + "/../secrets.JSON").read())['edamam_app_id']
APP_KEY = json.loads(open(DIR + "/../secrets.JSON").read())['edamam_app_key']

headers = {
}

params = {
    "app_id": APP_ID,
    "app_key": APP_KEY,
}

def get_recipe(base_food, start = 0, end = 100):
    qparams = {
        "from": start,
        "to": end,
        "q": base_food,
        **params
    }

    resp = requests.get("https://api.edamam.com/search", headers=headers, params=qparams)

    if resp.status_code != 200:
        return None

    resp = resp.content.decode('utf-8').replace('SUGAR.added', 'SUGAR_added')
    return json.loads(resp)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please input a food")
        exit()

    resp = get_recipe(sys.argv[1], end = 100)
    for item in resp['hits']:
        mongo_utils.add_recipe(item['recipe'])

