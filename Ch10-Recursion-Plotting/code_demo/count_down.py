def count_down(number):
    if number == 0:
        print('Done.')
    else:
        print(f'Count {number}')
        count_down(number - 1)


count_down(3)
