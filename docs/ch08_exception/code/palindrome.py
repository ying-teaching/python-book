# words is a list
if __name__ == "__main__":
    count = int(input("Please enter a count: "))
    words = ""
    for _ in range(count):
        word = input("Please enter a word: ")
        words += word.strip()

    reverse = words[::-1]
    if reverse == words:
        print("Yes")
    else:
        print("No")
