# Yiska Levi

def get_recipe_price(prices, optionals=None, **ingredients):
    total_price = 0

    for ingredient in ingredients:
        temp = True
        if optionals != None:
            if ingredient in optionals:
                temp = False
        if temp:
            total_price = total_price + ingredients.get(ingredient) * (prices[ingredient] / 100)

    return total_price

#A correctness test
print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
print(get_recipe_price({}))
