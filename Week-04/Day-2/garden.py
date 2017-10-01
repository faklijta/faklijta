class Garden(object):

    def __init__(self):
        self.flowers_trees = []

    def add(self, plant):
        self.flowers_trees.append(plant)
    
    def watering(self, amount):
        self.needs_water = []
        for plants in self.flowers_trees:
            if plants.water_status() == "needs water":
                self.needs_water.append(plants)
        for plants in self.needs_water:
            plants.watering(amount/len(self.needs_water)) 

    def status(self):
        for plant in self.flowers_trees:
            plant.printer()

        
class Plant(object):
    def __init__(self, color):
        self.amount_water = 0
        self.color = color
        self.plant_type = "plant"
        self.water_needed = 0
        self.absorbtion = 0

    def water_status(self):
        if self.amount_water < self.water_needed:
            return "needs water"
        else:
            return "does not need water"

    def watering(self, added_water):
        self.amount_water = added_water * self.absorbtion

    def printer(self):
        print("The " + self.color + " " + self.plant_type + " " + self.water_status())


class Tree(Plant):

    def __init__(self, color):
        super().__init__(color)
        self.water_needed = 10
        self.absorbtion = 0.4
        self.plant_type = "Tree"


class Flower(Plant):

    def __init__(self, color):
        super().__init__(color)
        self.water_needed = 5
        self.absorbtion = 0.75
        self.plant_type = "Flower"

garden = Garden()
garden.add(Flower("yellow"))
garden.add(Flower("blue"))
garden.add(Tree("purple"))
garden.add(Tree("orange"))
garden.status()
garden.watering(40)
garden.status()
garden.watering(70)
garden.status()
    