
from address import Address  

class Mailing:

    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = float(cost)
        self.track = str(track)

    def mail(self):
        print("Отправление", self.track,"из ИНД", self.from_address.ind, self.from_address.city, 
        self.from_address.street, "Дом", self.from_address.house, "кв -",self.from_address.flat, 
        "в ИНД", self.to_address.ind, self.to_address.city, self.to_address.street, "Дом",
        self.to_address.house, "кв -", self.to_address.flat, "Стоимость", self.cost, "рублей")
