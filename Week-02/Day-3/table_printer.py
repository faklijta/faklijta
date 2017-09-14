# Create a function that prints the ingredient list of dictionaries to the console in the following format:
#
# +--------------------+---------------+----------+
# | Ingredient         | Needs cooling | In stock |
# +--------------------+---------------+----------+
# | vodka              | Yes           | 1        |
# | coffee_liqueur     | Yes           | -        |
# | fresh_cream        | Yes           | 1        |
# | captain_morgan_rum | Yes           | 2        |
# | mint_leaves        | No            | -        |
# +--------------------+---------------+----------+

ingredients = [
	{ "name": "vodka", "in_stock": 1, "needs_cooling": True },
	{ "name": "coffee_liqueur", "in_stock": 0, "needs_cooling": True },
	{ "name": "fresh_cream", "in_stock": 1, "needs_cooling": True },
	{ "name": "captain_morgan_rum", "in_stock": 2, "needs_cooling": True },
	{ "name": "mint_leaves", "in_stock": 0, "needs_cooling": False },
	{ "name": "sugar", "in_stock": 0, "needs_cooling": False },
	{ "name": "lime juice", "in_stock": 0, "needs_cooling": True },
	{ "name": "soda", "in_stock": 0, "needs_cooling": True }
]
def table(ingredients):
    key = []
    for i in ingredients[0]:
        key.append(i)
    cooling = (key[2])
    stock = (key[1])
    name = []
    for j in ingredients:
        name.append(j["name"])
    print("+" + "--------------------" + "+" + "---------------" + "+" + "----------"* + "+\n")
    print("| Ingredient" + " " + "| Needs cooling | In stock |\n")
    print("+" + "--------------------" + "+" + "---------------" + "+" + "----------" + "+\n")
    for k in ingredients:
        fridge = ""
        if k["needs_cooling"]:
            frindge  = "Yes"
        else:
            fridge = "No"
        if k["in_stock"] == 0:
            k["in_stock"] = "-"
        print("| " + k["name"] + " " + "| " + fridge + " " + "| " + str(k["in_stock"]) + " " + "|\n")
    print("+" + "--------------------"+ "+" + "---------------" + "+" + "----------" + "+\n")
table(ingredients)
