"""
Author err1482 : Emerald Rafferty

Takes an ingredient and swaps it for an alternative ingredient based on the user dietary preferences

"""
from thewegmenu.utils.checker import has_meat, has_dairy, is_kosher, has_nuts, has_gluten, has_egg, has_soy
from thewegmenu.utils.wegmans_utils import get_skus, get_food_data, get_food_data_by_sku

def lactose_free(ingredient: str) -> bool:
    if has_dairy(ingredient):
        return False
    return True

def soy_free(ingredient: str) -> bool:
    if has_soy(ingredient):
        return False
    return True

def gluten_free(ingredient: str) -> bool:
    if has_gluten(ingredient):
        return False
    return True


def nut_free(ingredient: str) -> bool:
    if has_nuts(ingredient):
        return False
    return True


def kosher(ingredient: str) -> bool:
    if is_kosher(ingredient):
        return False
    return True


def vegetarian(ingredient: str) -> bool:
    if has_meat(ingredient):
        return False
    return True


"""TODO : make lists of alternatives for each category in replace and return that list instead"""
def vegan(ingredient: str) -> bool:
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
        return False
        # ingredient = vegetarian(ingredient)

    if has_dairy(ingredient):
        return False

    if has_egg(ingredient):
        return False

    return ingredient


# def replace(ingredient, pref) -> str:


"""
Facilitates the replacement of ingredients in a recipe to match dietary preferences. 
For now it just displays whether or not the ingredients are in the dietary preferences
@param recipe : a list of the ingredients in the recipe
@param pref : dietary preferences used to replace the recipe ingredients with ingredients that fit the preferences
"""
def main() -> list:
    # recipe: list, pref: list
    raw_recipe = {'cheese', 'chicken', "tofu"}
    pref = {'gluten free', 'vegetarian'}
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
        if'lactose free' in pref:
            if not lactose_free(i):
                recipe[i].update({'lactose free': False})



    # with open('ingredients.txt', 'finalRecipe') as outfile:
    #     json.dump(ingredients, outfile)

    print(recipe)
    return recipe


if __name__ == '__main__':
    main()
