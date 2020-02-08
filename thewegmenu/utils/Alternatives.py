"""
Author err1482 : Emerald Rafferty

Takes an ingredient and swaps it for an alternative ingredient based on the user dietary preferences

"""

import json

"""
checks to see if an ingredient is vegan, if not, it will return a
vegan alternative
"""
def vegan(ingredient:str) -> str:
    replace = {'milk': 'soymilk',
               'egg': 'Ener-G egg replacer',
               'beef': 'tofu',
               'turkey': 'tofu',
               'chicken': 'tofu',
               'pork': 'tofu',
               'gelatin': 'corn starch',
               'honey': 'agave nectar',
               'cheese':'Nutritional yeast flakes',
               'mayonnaise': 'grape seed oil mayonnaise',
                'ice cream': 'sherbet'
                }
    for i in replace:
        if i == ingredient:
            return replace[i]

    return ingredient


def main(recipe:list, pref:list) -> None:
    ingredients = {}

    for i in len(recipe):
        if 'vegan' in pref:
            i = vegan(i)

    # with open('ingredients.txt', 'finalRecipe') as outfile:
    #     json.dump(ingredients, outfile)


if __name__ == '__main__':
    main()
