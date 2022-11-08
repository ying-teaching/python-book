import random
random.seed(2022)
the_number = random.randint(0, 100)

while True:
    user_input = input('Please guess the number between 0 and 100: ')
    try:
        user_number = int(user_input)
        if user_number == the_number:
            print('Bingo.')
            break
        elif user_number > the_number:
            print('High.')
        else:
            print('Low.')
    except ValueError:
        print('Invalid input, please try again')
