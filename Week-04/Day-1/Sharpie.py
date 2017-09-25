class Sharpie(object):

    def __init__(self, color, width):
        self.color = str(color)
        self.width = float(width)
        self.ink_amount = 100
    
    def use(self):
        self.ink_amount -= 1

red_sharpie = Sharpie("red", 11)
red_sharpie.use()

print(red_sharpie.ink_amount, red_sharpie.color)

