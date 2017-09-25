class Counter(object):
    
    def __init__(self, default = 0):
        self.value = default
    
    def add(self, number= None):
        if number is None:
            self.value += 1
        else:
            self.value += int(number)
        
    def get(self):
        return self.value
    
    def reset(self):
        self.__init__()

