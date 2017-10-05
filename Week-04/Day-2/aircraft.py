class Aircraft(object):

    def __init__(self, aircraft_type):
        self.aircraft_type = aircraft_type
        self.ammo = 0
        if aircraft_type == 'F16':
            self.max_ammo = 8
            self.base_damage = 30
        if aircraft_type == 'F35':
            self.max_ammo = 12
            self.base_damage = 50

    def fight(self):
        current_ammo = self.ammo
        self.ammo = 0
        return self.base_damage * current_ammo

    def refill(amount_of_ammo):
        if self.ammo == self.max_ammo:
            return amount_of_ammo
        elif amount_of_ammo + self.ammo < self.max_ammo:
            self.ammo += amount_of_ammo
        else:
            self.ammo = self.max_ammo
            return amount_of_ammo - self.ammo
    
    def get_type(self):
        return self.aircraft_type
    
    def get_status(self):
        return "Type " + self.aircraft_type + " Ammo: " + self.ammo + " Base Damage: " + self.base.base_damage + " All Damage:" + self.fightfight


class Carrier(object):

    def __init__(self, store_ammo):
        self.aircrafts = []
        self.store_ammo = store_ammo
        self.health_point = 5000

    def add_aircraft(self, aircraft_type):
        self.aircrafts.append(aircraft_type)

    def fill(self):
        if self.ammo == 0:
            raise Exception ("No ammo!")
        for aircraft in self.aircrafts:
            if aircraft.aircraft_type == "F35":
                self.ammo = self.fill(self.ammo)
        for aircraft in self.aircrafts:
            self.ammo = self.refill(self.ammo)

    def fight(self, carrier):
        sum_of_damage = 0
        for aircraft in self.aircrafts:
            sum_of_damage += aircraft.fight()
            carrier.healt_point -= sum_of_damage
        
    def get_status(self):
        return"\nHP: {}, Aircraft count: {}, Ammo: {}, Total damage:".format(self.health_point, len(self.aircrafts), self.store_ammo)
        return"\n\nAircrafts:"
        for aircraft in self.aircrafts:
            return "\n" + str(aircraft.get_status())

mycarrier = Carrier(2300)

myaircraft = Aircraft("F35")
myaircraft2 = Aircraft("F16")
mycarrier.add_aircraft("F35")

print(mycarrier.get_status())
 


