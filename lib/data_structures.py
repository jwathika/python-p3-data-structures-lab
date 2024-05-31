spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    for food in spicy_foods:
        print(food["name"])


def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest_foods


def print_spicy_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 1]
    food_heat_levels = []
    for food in spiciest_foods:
        heat_level = ""
        for _ in range(food["heat_level"]):
            heat_level += "🌶"
        food_heat_levels.append(
            f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}"
        )
    return food_heat_levels


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass


def print_spiciest_foods(spicy_foods):
    pass


def get_average_heat_level(spicy_foods):
    pass


def create_spicy_food(spicy_foods, spicy_food):
    pass
