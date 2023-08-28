class InvalidNumber(Exception):
    def __init__(self, value):
        self.value = value


def take_inputs():
    try:
        user_input = input('Please enter a count: ')
        count = int(user_input)
    except:
        raise InvalidNumber(user_input)

    words = []
    for _ in range(count):
        word = input('Please enter word: ')
        words.append(word)

    return words


def is_palindrome(words):
    reverse = words[:]
    reverse.reverse()
    return reverse == words


if __name__ == '__main__':
    try:
        words = take_inputs()
        palindrome = is_palindrome(words)
        if palindrome:
            print('Yes')
        else:
            print('no')
    except InvalidNumber as e:
        print(f'The input is not valid number: {e}')
    except:
        print('oops, sorry for buggy app')
