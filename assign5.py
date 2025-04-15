#Assignment 1 : Design Your Own Class
#Question 1 and 2
class Smartphone:
    color = "Black"
    brand = "Apple"
    model = "iPhone 14"
    storage = 128

    def ring(self):
        print("The phone is ringing")
    def make_call(self):
        print("The phone is making a call")

my_smartphone = Smartphone()
my_smartphone.ring()
my_smartphone.make_call()  
print(my_smartphone.brand)

#Question 3 
class Smartphone:
    def __init__(self, color, brand, model, storage):
        self.color = color
        self.brand = brand
        self.model = model
        self.storage = storage
    def ring(self):
        print(f"{self.brand} {self.model} is ringing.")
    def make_call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}.")

phone1 = Smartphone("Black", "Apple", "iPhone 14", 128)
phone2 = Smartphone("White", "Samsung", "Galaxy S21", 256)

phone1.ring()
phone2.ring()
phone1.make_call("987-654-3210")
phone2.make_call("123-456-7890")
  
#Question 4
class SmartphoneZ(Smartphone):
    def __init__(self, color, brand, model, storage, price):
        super().__init__(color, brand, model, storage)
        self.price = price
    def take_photo(self):
        if self.storage > 200:
            self.storage -= 200
            print(f"Photo is taken with {self.price}$ camera on {self.model}.")
        else:
            print("Storage too low to take a photo.")
    def ring(self):
        print(f"{self.brand} {self.model} is playing a custom ringtone!.")

phone3 = SmartphoneZ("Blue", "Google", "Pixel 7", 228, 499.99)
phone3.take_photo()
phone3.ring()



#Activity 2 : Polymorphism Challenge
class Vehicle:
    def move (self):
        return "The vehicle moves..."
class Car(Vehicle):
    def move (self):
        return "Driving on the road."
class Plane(Vehicle):
    def move(self):
        return "Flying in the sky."
class Boat(Vehicle):
    def move(self):
        return "Sailing in the water!"
for Vehicle in (Car(), Plane(), Boat()):
    print(Vehicle.move())

   

    


    

