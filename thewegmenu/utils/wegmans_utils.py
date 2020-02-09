import requests, os, json, sys

MAX_RESULTS = 1
DIR = os.path.dirname(__file__) or '.'
KEY = json.loads(open(DIR + "/../secrets.JSON").read())['wegmans']

headers = {
    'Cache-Control': 'no-cache',
    "Subscription-Key": KEY,
}

params = {
    "api-version": "2018-10-18",
}


def get_skus(food):
    query = {
        "query": food,
        "results": MAX_RESULTS,
        **params,
    }

    resp = requests.get("https://api.wegmans.io/products/search/", headers=headers, params=query)

    if resp.status_code != 200:
        return None

    return [food['sku'] for food in json.loads(resp.content)['results']]

def get_food_data_by_sku(sku):
    resp = requests.get("https://api.wegmans.io/products/" + str(sku), headers=headers, params=params)
    if resp.status_code != 200:
        return None
    return json.loads(resp.content)

def get_food_data(food):
    skus = get_skus(food)
    if not skus:
        return None
    return list(filter(lambda x: x, [get_food_data_by_sku(sku) for sku in skus]))

if __name__ == '__main__':

    # if len(sys.argv) < 2:
    #     print("Please input a food")
    #     exit()
    # for item in get_food_data(sys.argv[1]):
    #      print(item['name'])
    # print("\n")
    #for item in get_food_data("vegan butter"):
    #     print(item)
    print(get_food_data_by_sku(11914))
