class InvalidNumber(Exception):
    def __init__(self, value):
        self.value = value


def take_inputs():
    try:
        user_input = input("Please enter a count: ")
        count = int(user_input)
    except:
        raise InvalidNumber(user_input)

    words = ""
    for _ in range(count):
        word = input("Please enter a word: ")
        words += word.strip()

    return words


def is_palindrome(words):
    reverse = words[::-1]
    if reverse == words:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    try:
        words = take_inputs()
        is_palindrome(words)
    except InvalidNumber as e:
        print(f"The input is not valid number: {e}")
    except:
        print("oops, sorry for buggy app")
