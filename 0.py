name = input('Hello! What is your name? ')

if name == 'Karol':
    print('Hello Karol!')
else:
    print('Hello', name, 'nice to meet you!')

age = int(input('How old are you? '))

if age >= 18:
    print("You are an adult, you are over 18 years old.")
else:
    print("You are underage, you aren't yet 18 years old.")
    z = 18 - age
    if z == 1:
        c = 'year.'
    if z >= 2:
        c = 'years.'
    print('You will be able to get a driving license in', z, c)