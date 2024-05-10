# student database 2

students = [
    {"name": "Tina", "hometown": "Portland", "favorite_food": "puppy chow"},
    {"name": "Klaus", "hometown": "Frankfurt", "favorite_food": "pizza"},
    {"name": "Julia", "hometown": "Houston", "favorite_food": "shrimp"}
]


def list_names(lst):
    for i in range(len(lst)):
        name = lst[i]['name']
        print(f'{i + 1}. {name}')
    return


def get_new_student():
    d = {'name': input('Type in a name: '),
         'hometown': input('Type in a hometown: '),
         'favorite_food': input('Type in a favorite food: ')
         }

    return d


def learn_about(d):
    # init vars
    name = d['name']
    food = d['favorite_food']
    city = d['hometown']

    # create while loop in case selection is wrong
    while True:
        # ask for hometown or food and get number
        selection = input(f'\nWould you like to learn about {name}\'s Hometown or Favorite Food?')
        # check selection
        if selection.lower() in 'favorite food':
            print(f'{name}\'s favorite food is {food}!')
            break
        elif selection.lower() in 'hometown':
            print(f'{name}\'s hometown is {city}!')
            break

        # error msg
        print('Sorry, this is not an option to learn about, try again!')


while True:
    print('Type in "add" to create a new student')
    print('Type in "view" to look at existing students')
    print('Type in "quit" to exit the program')

    ans = ''
    while True:
        if ans != 'add' or ans != 'view' or ans != 'quit':
            ans = input().lower()
        break

    if ans == 'add':
        students.append(get_new_student())

    if ans == 'view':
        # list names
        list_names(students)
        # ask for student index
        while True:
            s_num = input("\nWhich student would you like to learn about? ")
            if s_num.isnumeric() and 0 <= int(s_num) <= len(students):
                break
            print('Sorry, that\'s not one of the students, try again!')
        student_dict = students[int(s_num) - 1]
        s_name = student_dict['name']
        print(f'You have selected {s_name}!')
        learn_about(student_dict)

    if ans == 'quit':
        break

    print()
