# Heating/ Cooling

"""
Task: Write a function for a home thermostat.

Build Specifications:
Define a function named heating_cooling that takes in 2 parameters:
actual_temp and a desired_temp. Write conditionals to tell the heating & cooling system what to do.
Print one of these three things: Run A/C, Run heat, or Standby.

Call your function several times with different parameters in order to test it out.
At the end, prompt the user for actual and desired temperatures and use their inputs to call the function again.

"""


def heating_cooling(actual_temp, desired_temp):
    if actual_temp < desired_temp:
        return "Run Heat"
    if actual_temp > desired_temp:
        return "Run A/C"
    if actual_temp == desired_temp:
        return "Standby"


"""
Extended Challenge:
Define a function named convert_temp with 2 parameters: temp_celsius (a number) and target_unit 
(a string, either “C”, “F”, or “K”). Write a switch statement that checks the target_unit and 
returns the temperature converted to that unit. Notes: K stands for Kelvin. C requires no conversion, 
return the original temp.
"""


def convert_temp(temp_celsius, target_unit):
    if target_unit.lower() == 'c':
        return temp_celsius
    if target_unit.lower() == 'f':
        return (temp_celsius * 1.8) + 32
    if target_unit.lower() == 'k':
        return temp_celsius + 273.15


print(heating_cooling(65, 73))
print(heating_cooling(71, 71))
print(heating_cooling(80, 69))
print(convert_temp(50, 'F'))
print(convert_temp(37, 'K'))
print(convert_temp(71, 'C'))

actual = int(input('\nWhat is the actual temperature? '))
desired = int(input('What is the desired temperature? '))
print(heating_cooling(actual, desired))
