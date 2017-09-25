from Sharpie import Sharpie

class SharpieSet(object):

    def __init__(self):
        self.sharpies = []

    def count_usable(self):
        self.usable = 0
        for sharpie in self.sharpie_list:
            if sharpie.ink_amount > 0:
                self.usable += 1
        return sharpie.usable

    def remove_trash(self):
        for sharpie in self.sharpie_list:
            if sharpie.ink_amount == 0:
                self.sharpie.remove(sharpie)
        return self.sharpie

sharpie_list1 = SharpieSet
sharpie1 = Sharpie("red", 8.9)
print(sharpie_list1.count_usable)
print(sharpie_list1.remove_trash)
