# 2) Create 3 files in the classes directory car.py, fruit.py, and bank.py. Define the following classes in each module respectively. 
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.

# Discuss in your group and come up with the attributes and three methods (behaviours) for each class and implement them

# Then do the following in the interpreter 
# Create two instances of each class. 
# Call each of the methods you defined.
# Once you verify all the methods are working, commit your work, push to GitHub and submit.   

class Car:
    wheels = 4
    def __init__(self,make,model,year,mileage):
        self.make=make
        self.model=model
        self.year=year
        self.mileage=mileage
    def start(self):
        return f" The {self.make} is being driven"
    def stop(self):
        return f"The {self.make} has stopped"
    def get_mileage(self):
        return f"The {self.make} {self.model} has a mileage of{self.mileage}."
    def details(self):
        print(f"the {self.make} has {self.wheels} wheels")


car1 = Car("Toyota", "Corolla", 2019, 5000)
car2 = Car("Honda", "Civic", 2020, 2500)

print(car1.start())
print(car2.stop())

car1.get_mileage()
car2.get_mileage() 
car1.details()   
    

        
        