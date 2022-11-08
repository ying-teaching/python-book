from game import Game


def find_number(low, high, game):
    guess_number = (low + high) // 2
    check_result = game.check_number(guess_number)

    if check_result == 'Bingo':
        print(f'Bingo. The number is {guess_number}')
    elif check_result == 'Low':
        print(f'{guess_number} is too low. New range ({guess_number + 1}, {high})')
        find_number(guess_number + 1, high, game)
    else:
        print(f'{guess_number} is too high. New range ({low}, {guess_number - 1})')
        find_number(low, guess_number - 1, game)


if __name__ == '__main__':
    low = 0
    high = 100

    print(f'Find game from {low} to {high}')
    game = Game(low, high)
    find_number(low, high, game)
