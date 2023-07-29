class Address:

    def __init__(self, ind, city, street, house, flat):
        self.ind = ind
        self.city = city
        self.street = street
        self.house = house
        self.flat = flat
    def addr(self):
        print(self.ind, self.city, self.street, self.house, self.flat)