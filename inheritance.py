class Animal:
    
    def __init__(self, name):
        self.name = name
        print("Animals created")
    def get_name(self):
        print(self.name)


class Goat(Animal):
    def __init__(self, name):
        super().__init__(name)

goat = Goat('Lion')
goat.get_name()