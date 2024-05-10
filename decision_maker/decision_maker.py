# Decision Maker Lab

"""
Build Specifications:
1 Point: Use if/else statements to take different actions depending on user input.
Given an integer entered by a user, perform the following conditional actions:
1 Point: If the integer entered is odd and less than 60, print the number entered and “Odd and less than 60.”
1 Point: If the integer entered is even and in the inclusive range of 2 to 24, print “Even and less than 25.”
1 Point: If the integer entered is even and in the inclusive range of 26 to 60, print “Even and between 26 and 60 inclusive.”
1 Point: If the integer entered is even and greater than 60, print the number entered and “Even and greater than 60.”
1 Point: If the integer entered is odd and greater than 60, print the number entered and “Odd and greater than 60.”

Additional Requirements:
1 Point: For answering the Lab Summary when submitting to the LMS
-2 Points: if there are any syntax errors or if the program does not run (for example, in a Main method).
"""


def main():
    num = int(input('enter an integer between 1 and 100 inclusive: '))

    if num % 2 != 0:
        if num < 60:
            print(num, 'is odd and less than 60')
        elif num > 60:
            print(num, 'is odd and greater than 60')
    else:
        if 2 <= num <= 24:
            print(num, 'is even and less than 25')
        elif 26 <= num <= 60:
            print(num, 'is even and between 26 and 60 inclusive')
        elif num > 60:
            print(num, 'is even and greater than 60')


main()
