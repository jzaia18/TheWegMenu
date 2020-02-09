"""
Author err1482 : Emerald Rafferty

"""
from thewegmenu.utils.wegmans_utils import get_skus, get_food_data_by_sku

def has_pork(sku) -> bool:
    food_info = get_food_data_by_sku(sku)

    for i in food_info['ingredients']:
        if 'pork' in i.lower():
            return True
        if 'bacon' in i.lower():
            return True
    return False


def has_soy(sku) -> bool:
    food_info = get_food_data_by_sku(sku)

    for i in food_info['ingredients']:
        if 'soy' in i.lower():
            return True
    return False

def has_egg(sku) -> bool:
    food_info = get_food_data_by_sku(sku)

    for i in food_info['ingredients']:
        if 'egg' in i.lower():
            return True
    return False


def has_gluten(food: str) -> bool:
    sku = get_skus(food)
    food_info = get_food_data_by_sku(sku[0])

    for i in food_info['ingredients']:
        if 'gluten' in i.lower():
            return True
    return False


def is_kosher(sku) -> bool:
    food_info = get_food_data_by_sku(sku)

    if 'kshr' in food_info['name'].lower():
        return True
    return False


def has_nuts(sku) -> bool:
    food_info = get_food_data_by_sku(sku)

    for i in food_info['ingredients']:
        if 'tree nuts' in i.lower():
            return True
        if 'peanuts' in i.lower():
            return True

    return False


def has_meat(sku) -> bool:
    products = {'chicken', 'beef', 'pork', 'bacon', 'enzymes', 'meat'}

    food_info = get_food_data_by_sku(sku)

    print(food_info)

    for i in food_info['ingredients']:
        i = i.lower()
        for j in products:
            if j in i:
                return True

    return False

def has_dairy(food: str) -> bool:
    products = {'milk', 'cheese', 'contains milk', 'cheddar cheese'}

    sku = get_skus(food)
    food_info = get_food_data_by_sku(sku[0])

    for i in food_info['ingredients']:
        i = i.lower()
        for j in products:
            if j in i:
                return True
    return False


def main() -> None:
    print('meh')


if __name__ == '__main__':
    main()
