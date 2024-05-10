# Powers Table (Loops)

"""
Task: Pair program and display a table of powers.

What will the application do?
Prompt the user to enter an integer.
Display a table of squares and cubes from 1 to the value entered.
Ask if the user wants to continue.

Build Specifications
Assume that the user will enter valid data.
Only continue if the user agrees to.

Hints:
Don’t mess up the difference between squares and cubes!

"""


def main():

    while True:
        num = int(input('Enter an Integer: '))

        print('Number     Squared        Cubed')
        print('======     ========      =======')
        for n in range(1, num + 1):
            print(f'{n}            {n**2}            {n**3}')

        if input('\nContinue? (y/n)').lower() == 'n':
            print('Thanks!')
            break

        print()

main()
