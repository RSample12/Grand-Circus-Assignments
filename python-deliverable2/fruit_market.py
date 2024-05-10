# fruit_market.py
# Project 2

def main():
    table = [['Apple', 2], ['Grape', 1], ['Orange', 3]]
    order = {'Apple': 0, 'Grape': 0, 'Orange': 0}

    print('Welcome to the GC Fruit Market!')
    print('What is your name?')
    name = input()

    while True:
        print(f'\nWelcome {name}. Which Fruit would you like to buy?')
        for i, row in enumerate(table):
            print(f'{i + 1}. {row[0]} ${row[1]}')
        purchase = int(input())
        fruit = table[purchase - 1]
        order[fruit[0]] += 1

        print(f'You bought 1 {fruit[0].lower()} at ${fruit[1]}')

        print('Would you like to buy another piece of fruit? y/n')
        ans = input()
        while ans not in ['y', 'n']:
            print('Would you like to buy another piece of fruit? y/n')
            ans = input()

        if ans == 'n':
            print()
            break

    print(f'Order for {name}')
    total = 0
    for fruit in table:
        print(f'{order[fruit[0]]} {fruit[0].lower()}(s) at ${fruit[1]} apiece')
        fruit_total = order[fruit[0]] * fruit[1]
        total += fruit_total

    print(f'Sub Total: ${total}')
    print(f'5% Tax: ${0.05 * total}')
    print(f'Total: ${1.05 * total}')

    return


main()
