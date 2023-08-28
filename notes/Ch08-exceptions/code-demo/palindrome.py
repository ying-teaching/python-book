# words is a list
if __name__ == '__main__':
    count = int(input('Please enter a count: '))
    for _ in range(count):
        words = []
        word = input('Pleaes enter a word: ')
        words.append(word)

    reverse = words[:]
    reverse.reverse()
    if reverse == words:
        print('Yes')
    else:
        print('No')
