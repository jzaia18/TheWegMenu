"""
Author err1482 : Emerald Rafferty

Takes an ingredient and swaps it for an alternative ingredient based on the user dietary preferences

"""
from thewegmenu.utils.wegmans_utils import get_skus, get_food_data, get_food_data_by_sku

"""
checks to see if an ingredient is vegan, if not, it will return a
vegan alternative ingredient
"""

"""TODO : make lists of alternatives for each category in replace and return that list instead"""


def vegan(ingredient: str) -> str:
    replace = {'milk': 'Wegmans Organic Original Soymilk',
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

    sku = get_skus(ingredient)
    food_info = get_food_data_by_sku(sku[0])

    for i in food_info['ingredients']:
        i = i.strip('.').strip(',').lower()
        print(i)
        if i in replace:
            return replace[i]

    for i in replace:
        if i in food_info['ingredients']:
            print(i);
            print(replace[i])
            return replace[i]

    return food_info['name']


"""
Facilitates the replacement of ingredients in a recipe to match dietary preferences. 

@param recipe : a list of the ingredients in the recipe
@param pref : dietary preferences used to replace the recipe ingredients with ingredients that fit the preferences
"""


def main() -> None:
    # recipe: list, pref: list
    recipe = {'milk', 'ground beef'}
    pref = {'vegan'}
    # for i in recipe:
    #     if 'vegan' in pref:
    #         i = vegan(i)
    #
    # for i in recipe:
    #     print(i)

    print(vegan('cheese'))
    print(vegan('chicken'))


    # print(vegan('ground beef'))
    # with open('ingredients.txt', 'finalRecipe') as outfile:
    #     json.dump(ingredients, outfile)


if __name__ == '__main__':
    main()
