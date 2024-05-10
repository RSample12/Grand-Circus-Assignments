# Student Database

name = ['Riley', 'Alex', 'Diego']
city = ['Austin', 'Houston', 'San Antonio']
food = ['Pizza', 'Ramen', 'Beans']

cont = 'y'
while cont != 'n':
    # print names in lst according to index
    for i in range(len(name)):
        print(f'{i + 1}. {name[i]}')

    # ask for student index
    while True:
        student = int(input("\nWhich student would you like to learn about? ")) - 1
        if 0 <= student <= len(name):
            break
        print('Sorry, that\'s not one of the students, try again!')
    print(f'You have selected {name[student]}!')

    # create while loop in case selection is wrong
    while True:
        # ask for hometown or food and get number
        selection = input(f'\nWould you like to learn about {name[student]}\'s Hometown or Favorite Food?')
        # check selection
        if selection.lower() in 'favorite food':
            print(f'{name[student]}\'s favorite food is {food[student]}!')
            break
        elif selection.lower() in 'hometown':
            print(f'{name[student]}\'s hometown is {city[student]}!')
            break

        # error msg
        print('Sorry, this is not an option to learn about, try again!')

    # break if n or N
    while True:
        cont = input('\nWould you like to learn about another student? Y/N: ')
        if cont.lower() == 'y' or cont.lower() == 'n':
            break
        print('Sorry, try again!')

    print()

print('Thanks for playing!')
