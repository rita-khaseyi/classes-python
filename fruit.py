class Fruit:
    is_ripe = True


    def __init__(self, name, color, taste):
        self.name = name
        self.color = color
        self.taste = taste
    def fruit(self):
        print(f"The {self.name} is {self.color} and tastes {self.taste}.")

    def is_edible(self):
        if self.taste == "sweet" or self.taste == "sour":
            print(f"The {self.name} is edible.")
        else:
            print(f"The {self.name} is not edible.")
fruit1 = Fruit("Apple", "Red", "Sweet")
fruit2 = Fruit("Lemon", "Yellow", "Sour")

fruit1.fruit()
fruit2.is_edible()  
          



