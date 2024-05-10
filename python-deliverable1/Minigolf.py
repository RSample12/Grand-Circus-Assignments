# Minigolf.py
# Python Project 1

def main():
    name = input('Welcome to GC mini golf! What is your name? ')

    holes = 0
    while holes not in [3, 6]:
        holes = int(input(f'Hi, {name}! Would you like to play 3 or 6 holes today? '))

    total = 0
    for i in range(1, holes + 1):
        putts = int(input(f'How many putts for hole {i}? (par is 3) '))
        total += putts

    par = (3 * holes)
    score = total - par
    if score > 0:
        print(f'Nice try, {name}... Your total score was: +{score}')
    elif score < 0:
        print(f'Great job, {name}! Your total score was: {score}')
    else:
        print(f'Good game, {name}. Your total score was: 0')

    return


main()
