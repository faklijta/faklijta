class Sharpie(object):

    def __init__(self, color, width):
        self.color = str(color)
        self.width = float(width)
        self.ink_amount = 100
    
    def use(self):
        self.ink_amount -= 1

class SharpieSet(object):

    def __init__(self):
        pass

    def count_usable(self):
        if sharpie.ink_amount > 0:
        return sharpie.color()

    def remove_trash(self):
        if sharpie.ink_amount == 0:
            pass
