def calculate (**kwarg):
    print (type (kwarg)) # Dictionary
    for key, value in kwarg.items ():
        print (key)
        print (value)

calculate (add= 3, multiply = 5) # This is not adding or multiplying numbers, Just for see what happening.

print ("----------------")

def calc (n = 0, **kwarg):
    # n += kwarg ["add"]
    n *= kwarg ["multiply"]
    n += kwarg.get("add") # Another way
    print (n)

calc (2, add = 3, multiply= 3)

print ("----------------")

# You can make this also with classes

class car:
    def __init__(self, **kwarg):
        self.make = kwarg.get ("make")
        self.model = kwarg.get ("model")
        self.color = kwarg.get ("color")
        self.seats = kwarg.get ("seats")    


my_car = car (make= "Nissan", model= "GT-R", seats = 4)
my_car2 = car (make= "BMW", color = "black")


print (my_car.make, my_car.model, my_car.color, my_car.seats)

print (my_car2.make, my_car2.model, my_car2.color, my_car2.seats)



