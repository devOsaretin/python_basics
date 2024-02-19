class Dog:
    def __init__(self, breed, name, has_spot):
        self.breed = breed
        self.name = name
        self.has_spot = has_spot

    def bark(self):
        return 'Woo Woo'


my_dog = Dog("German Shephard", "Sharon", True)
print(my_dog.breed)
print(my_dog.bark())

my_dog2 = Dog('Chihuahua', "Luiy", False)
print(my_dog2.name)