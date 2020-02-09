"""
Author err1482 : Emerald Rafferty

"""
from thewegmenu.utils.wegmans_utils import get_skus, get_food_data_by_sku


def has_gluten(food:str) ->bool:
    sku = get_skus(food)
    food_info = get_food_data_by_sku(sku[0])

    for i in food_info['ingredients']:
        if 'gluten' in i.lower():
            return True
    return False

def is_kosher(food:str) -> bool:
    sku = get_skus(food)
    food_info = get_food_data_by_sku(sku[0])

    if 'kshr' in food_info['name'].lower():
        return True
    return False

def has_nuts(food:str) -> bool:
    sku = get_skus(food)
    food_info = get_food_data_by_sku(sku[0])

    for i in food_info['ingredients']:
        if 'tree nuts' in i.lower():
            return True
        if 'peanuts' in i.lower():
            return True

    return False


def has_meat(food:str) -> bool:
    sku = get_skus(food)
    food_info = get_food_data_by_sku(sku[0])

    return not (food_info['isLactoovoVegetarian'])

def has_dairy(food:str) -> bool:

    products = {'milk', 'cheese', 'contains milk', 'cheddar cheese'}

    sku = get_skus(food)
    food_info = get_food_data_by_sku(sku[1])

    for i in food_info['ingredients']:
        for j in i.split(' '):
            j = j.strip('.').strip('(').strip(')').strip(',').lower()
            if j in products:
                return True
        #print("\n")
    return False



def main() -> None:
    print('meh')

if __name__ == '__main__':
    main()