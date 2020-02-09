"""
Author err1482 : Emerald Rafferty

Takes an ingredient and swaps it for an alternative ingredient based on the user dietary preferences

"""
from utils.checker import has_meat, has_dairy, is_kosher, has_nuts, has_gluten, has_egg, has_soy
from utils.wegmans_utils import get_skus, get_food_data, get_food_data_by_sku


def lactose_free(ingredient) -> bool:
    if has_dairy(ingredient):
        return False
    return True


def soy_free(ingredient) -> bool:
    if has_soy(ingredient):
        return False
    return True


def gluten_free(ingredient) -> bool:
    if has_gluten(ingredient):
        return False
    return True


def nut_free(ingredient) -> bool:
    if has_nuts(ingredient):
        return False
    return True


def kosher(ingredient) -> bool:
    if is_kosher(ingredient):
        return True
    return False


def vegetarian(ingredient) -> bool:
    if has_meat(ingredient):
        return False
    return True


"""TODO : make lists of alternatives for each category in replace and return that list instead"""


def vegan(ingredient) -> bool:

    if has_meat(ingredient):
        return False

    if lactose_free(ingredient):
        return False

    if has_egg(ingredient):
        return False

    return True


# def replace(ingredient, pref) -> str:


"""
Facilitates the replacement of ingredients in a recipe to match dietary preferences. 
For now it just displays whether or not the ingredients are in the dietary preferences
@param recipe : a list of the ingredients in the recipe
@param pref : dietary preferences used to replace the recipe ingredients with ingredients that fit the preferences
"""


def filter_recipe(raw_recipe: list, pref: list) -> list:

    recipe = {}
    for i in raw_recipe:
        food_info = get_food_data_by_sku(i)
        if food_info is None:
            continue
        recipe.update({food_info['name']: {}})
        i = food_info['name']
        if 'kosher' in pref:
            if not is_kosher(food_info):
                recipe[i].update({'kosher': False})
        if 'gluten_free' in pref:
            if has_gluten(food_info):
                recipe[i].update({'gluten_free': False})
        if 'vegan' in pref:
            if not vegan(food_info):
                recipe[i].update({'vegan': False})
        if 'nut_free' in pref:
            if has_nuts(food_info):
                recipe[i].update({'nut_free': False})
        if 'vegetarian' in pref:
            if has_meat(food_info):
                recipe[i].update({'vegetarian': False})
        if 'soy_free' in pref:
            if has_soy(food_info):
                recipe[i].update({'soy_free': False})
        if 'lactose_free' in pref:
            if has_dairy(food_info):
                recipe[i].update({'lactose_free': False})

    print(recipe)
    return recipe


if __name__ == '__main__':
    pass
