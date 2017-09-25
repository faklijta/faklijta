class Animals(object):

    def __init__(self, hunger, thirst):
        self.thirst = thirst
        self.hunger = hunger

    def eat(self):
        self.hunger -= 1
    
    def drink(self):
        self.thirst -= 1
    
    def play(self):
        self.hunger += 1
        self.hunger += 1