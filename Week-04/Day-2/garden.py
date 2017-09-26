class Garden(object):

    def __init__(self):
        self.flowers_trees = []

    def add(self, plant):
        self.flowers_trees.append(plant)
    
    def watering(self, watering_amount):
        self.plants_to_water = []
        # for plant in self.flowers_trees:
        #     if plant
    
    
class Flower(object):

    def __init__(self, color):
        self.water_amount = 0
        self.color = color
    
    def water_need(self):
        if self.water_need < 5:
            return "needs water"

    def watering(self, watering_amount):
        self.water_amount = watering_amount* 0.7
    
class Trees(object):

    def __init__(self, color):
    self.water_amount = 0
    self.color = color

    def water_need(self):
        if self.water_need < 10:
            return "needs water"
    
    def watering(self, watering_amount):
        self.water_amount = watering_amount * 0.4




    