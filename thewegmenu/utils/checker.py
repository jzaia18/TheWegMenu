"""
Author err1482 : Emerald Rafferty

"""

def has_pork(food_info) -> bool:
    for i in food_info['ingredients']:
        if 'pork' in i.lower():
            return True
        if 'bacon' in i.lower():
            return True
    return False


def has_soy(food_info) -> bool:
    for i in food_info['ingredients']:
        if 'soy' in i.lower():
            return True
    return False

def has_egg(food_info) -> bool:
    for i in food_info['ingredients']:
        if 'egg' in i.lower() and 'veg' not in i.lower():
            return True
    return False


def has_gluten(food_info) -> bool:
    for i in food_info['ingredients']:
        if 'gluten' in i.lower():
            return True
    return False


def is_kosher(food_info) -> bool:
    if 'kshr' in food_info['name'].lower():
        return True
    if has_pork(food_info):
        return False
    return True


def has_nuts(food_info) -> bool:
    for i in food_info['ingredients']:
        if 'tree nuts' in i.lower():
            return True
        if 'peanuts' in i.lower():
            return True

    return False


def has_meat(food_info) -> bool:
    products = {'chicken', 'beef', 'pork', 'bacon', 'enzymes', 'meat', 'fish'}
    for i in food_info['ingredients']:
        i = i.lower()
        for j in products:
            if j in i:
                return True
    return False

def has_dairy(food_info) -> bool:
    products = {'milk', 'cheese', 'contains milk', 'cheddar cheese'}

    for i in food_info['ingredients']:
        i = i.lower()
        for j in products:
            if j in i and 'coconut' not in i and 'soy' not in i and 'almond' not in i and 'oat' not in i and 'rice' not in i:
                return True
    return False


def main() -> None:
    print('meh')


if __name__ == '__main__':
    main()
