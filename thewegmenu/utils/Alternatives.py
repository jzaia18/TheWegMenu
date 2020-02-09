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
        return False
    return True


def vegetarian(ingredient) -> bool:
    if has_meat(ingredient):
        return False
    return True


"""TODO : make lists of alternatives for each category in replace and return that list instead"""


def vegan(ingredient) -> bool:

    if has_meat(ingredient):
        return False

    if has_dairy(ingredient):
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
        recipe.update({i: {}})

    for i in raw_recipe:
        if 'kosher' in pref:
            if not kosher(i):
                recipe[i].update({'kosher': False})
        if 'gluten free' in pref:
            if not gluten_free(i):
                recipe[i].update({'gluten free': False})
        if 'vegan' in pref:
            if not vegan(i):
                recipe[i].update({'vegan': False})
        if 'nut free' in pref:
            if not nut_free(i):
                recipe[i].update({'nut free': False})
        if 'vegetarian' in pref:
            if not vegetarian(i):
                recipe[i].update({'vegetarian': False})
        if 'soy free' in pref:
            if not soy_free(i):
                recipe[i].update({'soy free': False})
        if 'lactose free' in pref:
            if not lactose_free(i):
                recipe[i].update({'lactose free': False})

    # with open('ingredients.txt', 'finalRecipe') as outfile:
    #     json.dump(ingredients, outfile)

    print(recipe)
    return recipe


if __name__ == '__main__':
    pass
