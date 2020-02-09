"""

"""
from utils.wegmans_utils import get_food_data


def find_weggie(food: str) -> tuple:
    food = get_food_data(food)

    if not food:
        return (None, None)

    return (food[0]['name'], food[0]['sku'])

def translate(ingredients: list) -> tuple:
    recipe = []
    for i in ingredients:
        recipe.append(find_weggie(i))

    return recipe


if __name__ == '__main__':
    pass
