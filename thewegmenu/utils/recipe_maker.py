"""

"""
from thewegmenu.utils.wegmans_utils import get_food_data


def find_weggie(food: str) -> tuple:
    food = get_food_data(food)

    return (food['name'], food['sku'])

def translate(ingredients: list) -> tuple:
    recipe = []
    for i in ingredients:
        recipe.append(find_weggie(i))

    return recipe


if __name__ == '__main__':
    pass