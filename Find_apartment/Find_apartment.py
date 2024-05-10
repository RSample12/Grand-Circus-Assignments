# Find an Apartment

"""
Task: Create and call several functions, using a combination of default parameters,
named arguments, and lambda functions.
"""


# returns apt search string with customer preference
def apt_search1(city, max_rent, min_beds, pets_allowed):
    if pets_allowed:
        pets = ' that allow pets'
    else:
        pets = ''

    return f'Welcome to RS Property Management! Looking up listings in the {city} ' \
           f'area for {min_beds} bedroom apartments{pets}, all within a ${max_rent} budget...'


print('apt_search1')
print(apt_search1('Austin', 1500, 2, True))
print(apt_search1('New York', 3000, 1, False))


# returns apt search string with customer preference, 1 bed default, no pets default
def apt_search2(city, max_rent, min_beds=1, pets_allowed=False):
    if pets_allowed:
        pets = ' that allow pets'
    else:
        pets = ''

    return f'Welcome to RS Property Management! Looking up listings in the {city} ' \
           f'area for {min_beds} bedroom apartments{pets}, all within a ${max_rent} budget...'


print('\napt_search2')
print(apt_search2('Dallas', 1200))
print(apt_search2('Houston', 1400, min_beds=3))
print(apt_search2('Boston', 4200, min_beds=2, pets_allowed=True))


# Lambda Functions
print('\nLambda functions')
plus_onehundred = lambda n: n + 100
print(plus_onehundred(56))
squared = lambda n: n ** 2
print(squared(5))
concatenate = lambda s: '- ' + s
print(concatenate('Hello, World!'))
divide_by_three = lambda n: n / 3
print(divide_by_three(18))
