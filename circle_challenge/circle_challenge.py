# Circle Challenge
# Create a class named Circle to store the data about this circle.
import math


class circle():
    def __init__(self, radius):
        self.radius = radius

    # Returns the calculated diameter
    def calculate_diameter(self):
        return 2 * self.radius
   
    # Returns the calculated circumference
    def calculate_circumference(self):
        return math.pi * self.calculate_diameter()
    
    # Returns the calculated area
    def calculate_area(self):
        return math.pi * (self.radius**2)
   
    # Doubles the radius property
    def grow(self):
        self.radius = self.radius * 2
   
    # Returns the radius value
    def get_radius(self):
        return self.radius
    
    def __str__(self):
        return(f'Diameter: {self.calculate_diameter()}\nCircumference: {self.calculate_circumference()}\nArea: {self.calculate_area()} \n')
    
radius = int(input('Enter a radius: '))
circle1 = circle(radius)
print(circle1)

while True:
    ans = input('Would you like your circle to grow? (y/n) ').lower()

    if ans == 'n':
        print('Goodbye')
        break
    if ans == 'y':
        print('Stand by while your cirlce magically grows...')
        circle1.grow()
        print(circle1)
    else:
        print('Wrong input, try again...')