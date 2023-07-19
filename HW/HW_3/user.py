class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def seyF_name(self):
        print("мое имя", self.first_name)

    def sayL_name(self):
        print("Моя фамилия", self.last_name)

    def sayFL_name(self):
        print("Мое имя и фамилия", self.first_name, self.last_name)            
