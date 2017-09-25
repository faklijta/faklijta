class Animals(object):

    def __init__(self):
        self.thirst = 50
        self.hunger = 50

    def eat(self):
        self.hunger -= 1
        print(self.hunger)
    
    def drink(self):
        self.thirst -= 1
        print(self.thirst)
    
    def play(self):
        self.hunger += 1
        self.hunger += 1
        print(self.hunger, self.thirst)
