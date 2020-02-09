"""
Author err1482 : Emerald Rafferty

Takes an ingredient and swaps it for an alternative ingredient based on the user dietary preferences

"""
from thewegmenu.utils.checker import has_meat, has_dairy, is_kosher, has_nuts, has_gluten, has_egg
from thewegmenu.utils.wegmans_utils import get_skus, get_food_data, get_food_data_by_sku

def gluten_free(ingredient: str) -> str:
    if has_gluten(ingredient):
        return ingredient + ' not gluten free'
    return ingredient + ' is gluten free'


def nut_free(ingredient: str) -> str:
    if has_nuts(ingredient):
        return ingredient + ' is not nut free'
    return ingredient


def kosher(ingredient: str) -> str:
    if is_kosher(ingredient):
        return ingredient + ' is kosher'
    return ingredient + ' not kosher'


def vegetarian(ingredient: str) -> str:
    if has_meat(ingredient):
        return 'Wegmans Organic Firm Tofu'
    return ingredient


"""TODO : make lists of alternatives for each category in replace and return that list instead"""


def vegan(ingredient: str) -> str:
    replace = {'milk': 'Wegmans Organic Original Soymilk',
               'contains milk': 'recipe: list, pref: list',
               'egg': 'Namaste Raw Goods Egg Replacer',
               'beef': 'Wegmans Organic Firm Tofu',
               'turkey': 'Wegmans Organic Firm Tofu',
               'chicken': 'Wegmans Organic Firm Tofu',
               'pork': 'Wegmans Organic Firm Tofu',
               'gelatin': 'Wegmans 100% Pure Cornstarch',
               'honey': 'Agave In The Raw Agave Nectar, Organic',
               'cheese': 'Follow Your Heart Vegan Gourmet Cheese Alternative, Mozzarella',
               'mayonnaise': 'Hellmann\'s Dressing & Sandwich Spread, Vegan',
               'ice cream': 'sherbet'}

    if has_meat(ingredient):
        return ingredient + ': not vegan'
        # ingredient = vegetarian(ingredient)

    if has_dairy(ingredient):
        return ingredient + ': not vegan'

    if has_egg(ingredient):
        return ingredient + ': not vegan'

    return ingredient


# def replace(ingredient, pref) -> str:


"""
Facilitates the replacement of ingredients in a recipe to match dietary preferences. 

@param recipe : a list of the ingredients in the recipe
@param pref : dietary preferences used to replace the recipe ingredients with ingredients that fit the preferences
"""


def main() -> list:
    # recipe: list, pref: list
    recipe = {'cheese', 'ground beef', 'whole wheat bread', 'egg'}
    pref = {'kosher', 'gluten free', 'vegan'}
    for i in recipe:
        if 'kosher' in pref:
            print(kosher(i))
        if 'gluten free' in pref:
            print(gluten_free(i))
        if 'vegan' in pref:
            print(vegan(i))

    # with open('ingredients.txt', 'finalRecipe') as outfile:
    #     json.dump(ingredients, outfile)

    return recipe


if __name__ == '__main__':
    main()
