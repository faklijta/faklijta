class Station(object):
    def __init__(self):
        self.gas_amount = 2000

    def refill(self, car):
        self.gas_amount -= car.gas_capacity
        car.gas_amount += car.gas_capacity

class Car(object):
    def __init__(self):
        self.gas_amount = 0
        self.gas_capacity = 100

car1 = Car()
station1 = Station()

station1.refill(car1)
print(car1.gas_amount)
print(station1.gas_amount)
