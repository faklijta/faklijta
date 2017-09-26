class Garden(object):

    def __init__(self):
        self.flowers_trees = []

    def add(self, plant):
        self.flowers_trees.append(plant)
    
    def watering(self, amount):
        self.needs_water = []
        for plants in self.flowers_trees:
            if plants.water_need() == "needs water":
                self.needs_water.append(plants)
        for plants in self.needs_water:
            plants.watering(amount/len(self.needs_water))
        return self
    
    def __repr__(self):
        all_plants = ""
        for plant in range(len(self.flowers_trees)):
             all_plants += str(self.flowers_trees[plant]) + "\n"
        return all_plants


class Plant(object):
    def __init__(self, color, amount=0):
        self.amount = amount
        self.color = color
        self.watering_index = 0


class Flower(Plant):

    def water_need(self):
        if self.amount < 5:
            return "needs water"
        else:
            return "does not needs water"

    def watering(self, amount=0):
        self.amount += amount * 0.75

    def __repr__(self):
        return "The {} flower {}.".format(self.color, self.water_need())


class Trees(Plant):

    def water_need(self):
        if self.amount < 10:
            return "needs water"
        else:
            return "does not needs water"
    
    def watering(self, amount = 0):
        self.amount += amount * 0.4
    
    def __repr__(self):
        return "The {} tree {}.".format(self.color, self.water_need())

garden = Garden()
garden.add(Flower("yellow"))
garden.add(Flower("blue"))
garden.add(Trees("purple"))
garden.add(Trees("orange"))
print(garden)
garden.watering(40)
print(garden)
garden.watering(70)
print(garden)
    