# oop under 20 minute from youtube channel Indently

class Microwave:
    # self is a reference to the current instance of the class. It allows you to access instance variables and methods within the class.
    # self is turned into Smeg when Smeg is called. It refers to the instance of the class that is being created or manipulated. self = smeg
    def __init__(self,brand : str, power_rating: str) -> None:
        self.brand = brand
        self.power_rating = power_rating
    
    def turn_on(self) -> None:
        if self.turned_on:
            print(f"{self.brand} microwave is already on.")
        else:
            self.turned_on = True
            print(f"{self.brand} microwave is now on.")     
               
    def turn_off(self) -> None:
        if self.turn_off:
            print(f"{self.brand} microwave is already off.")
        else:
            self.turn_off = True
            print(f"{self.brand} microwave is now off.")     
               
smeg: Microwave = Microwave(brand="Smeg", power_rating="800W")
print(smeg.power_rating)

# bosch: Microwave = Microwave(brand="Bosch", power_rating="900W")
# print(bosch.power_rating)   