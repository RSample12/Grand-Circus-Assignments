# Car dealership
"""
What will the application do?
Prompt the user to choose from different categories of vehicle to compare for purchase.
Display an error if the user enters invalid data and asks the user again for a selection.
When the user enters valid data, print each vehicle within that collection of their choosing.
Ask the user if they would like to add a vehicle to compare.
If yes, the user will make a selection and that vehicle will be placed in a collection containing for them to later “compare”.
If not, give the user the option to look at more vehicles in other categories or go ahead and “compare vehicles”.
The user will receive a detailed list of all chosen vehicles, listing their make, miles, and price. 
Each vehicle should also “make noise” as the program iterates through the list.
"""

# Build Specifications:
# Create a base class named Vehicle to store the data about each vehicle.
# Initialization (self, make, miles, price)
class Vehicle():
    def __init__(self, make, miles, price):
        # Sets the make, miles and price properties
        self.make = make
        self.miles = miles
        self.price = price
        # Also sets a engine_on property to False
        engine_on = False

    # start_engine()
    def start_engine(self):
        # Prints a message: “Starting engine…”
        print('Starting engine...')
        self.engine_one = True
    
    # make_noise()
    def make_noise(self):
        # Prints a message: “Beep beep!”
        print('Beep beep!')


# Create a derived class from Vehicle named Truck to store the data about each vehicle.
class Truck(Vehicle):
    # Initialization (self, make, miles, price)
    def __init__(self, make, miles, price):
        # Sets the make, miles and price properties
        Vehicle.__init__(self, make, miles, price)
        # Also sets a cargo property to False
        self.cargo = False

    # load_cargo()
    def load_cargo(self):
        # Prints a message: “Loading the truck bed…”
        # Sets cargo to True
        print('Loading cargo...')
        self.cargo = True


# Create a derived class from Vehicle named Motorcycle to store the data about each vehicle. This class should contain these specifications:
class Motorcycle(Vehicle):
    # Initialization (self, make, miles, price, top_speed)
    def __init__(self, make, miles, price, top_speed):
        # Sets the make, miles and price properties
        # Sets additional method of top_speed
        Vehicle.__init__(self, make, miles, price)
        self.top_speed = top_speed

    # make_noise()
    def make_noise(self):
        # Prints a message: “Vroom vroom!”
        print('Vroom vroom!')


def list_vehicles(arr, bike, noise):
    s = ''
    for i, j in enumerate(arr):
        if bike:
            s =  f'and a top speed of {j.top_speed} ' 
        print(f'{i+1}: {j.make}: with {j.miles} {s}costs ${j.price}')

        if noise:
            j.make_noise()


# Create two lists: bikes, and trucks. 
# Create at least 3 instances of both subclasses and store in the appropriate list.
bike1 = Motorcycle('Yamaha', 15056, 5250, 120)
bike2 = Motorcycle('Harley-Davidson', 25670, 8000, 100)
bike3 = Motorcycle('Honda', 80001, 2500, 75)
bikes = [bike1, bike2, bike3]

truck1 = Truck('GMC', 95000, 45000)
truck2 = Truck('Ford', 145000, 25000)
truck3 = Truck('Chevy', 189000, 18000)
trucks = [truck1, truck2, truck3]

# Create an empty list named vehicles_to_compare and fill with the user’s selection(s).
vehicles_to_compare = []
while True:
    # ask for bikes or trucks
    while True:
        vtype = input('Would you like to see bikes or trucks? (b/t)\n').lower()
        if vtype == 'b':
            list_vehicles(bikes, True, False)
            break
        if vtype == 't':
            list_vehicles(trucks, False, False)
            break
        else:
            print('Please select \'b\' or \'t\'')
    
    # ask if you would like to continue
    while True:
        selection = input('Would you like to compare one of these vehicles today? (y/n)\n')
        if selection == 'y' or selection == 'n':
            break
        print('Please select \'y\' or \'n\'')
    
    # ask for vnum from list
    if selection == 'y':
        while True:
            vnum = int(input('Which vehicle would you like to compare today? (Please list number)\n'))
            if 0 < vnum < 4:
                break
        
    elif selection =='n':
        continue

    if vtype == 'b':
        vehicles_to_compare.append(bikes[vnum-1])
        print(f'{bikes[vnum-1].make} added!')
    if vtype == 't':
        vehicles_to_compare.append(trucks[vnum-1])
        print(f'{trucks[vnum-1].make} added!')

    # ask if you would like to continue
    while True:
        selection = input('Would you like to compare your vehicles now? (y/n)\n')
        if selection == 'y' or selection == 'n':
            break
        print('Please select \'y\' or \'n\'')

    # if y, break loop and compare, if no, repeat loop
    if selection == 'y':
        break
        
    elif selection =='n':
        continue


print('Here are your vehicles to compare: ')
list_vehicles(vehicles_to_compare, False, True)
print('Thank you and have a nice day!')


            
