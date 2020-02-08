"""
Author err1482 : Emerald Rafferty

Takes an ingredient and swaps it for an alternative ingredient based on the user dietary preferences

"""
from thewegmenu.utils.wegmans_utils import get_skus, get_food_data, get_food_data_by_sku

"""
checks to see if an ingredient is vegan, if not, it will return a
vegan alternative ingredient
"""


def vegan(ingredient: str) -> str:
    replace = {'milk': 'soymilk',
               'egg': 'Ener-G egg replacer',
               'beef': 'tofu',
               'turkey': 'tofu',
               'chicken': 'tofu',
               'pork': 'tofu',
               'gelatin': 'corn starch',
               'honey': 'agave nectar',
               'cheese': 'Nutritional yeast flakes',
               'mayonnaise': 'grape seed oil mayonnaise',
               'ice cream': 'sherbet'}

    sku = get_skus(ingredient)
    food_info = get_food_data_by_sku(sku[0])
    food = get_food_data(ingredient)


    if 'ingredients' in food_info:
        for i in food_info['ingredients']:
            if i in replace:
               print("here")

    return ingredient


"""
Facilitates the replacement of ingredients in a recipe to match dietary preferences. 

@param recipe : a list of the ingredients in the recipe
@param pref : dietary preferences used to replace the recipe ingredients with ingredients that fit the preferences
"""


def main() -> None:
 #   recipe: list, pref: list
 #    for i in len(recipe):
 #        if 'vegan' in pref:
 #            i = vegan(i)

    vegan('triscuit')
    # with open('ingredients.txt', 'finalRecipe') as outfile:
    #     json.dump(ingredients, outfile)


if __name__ == '__main__':
    main()
