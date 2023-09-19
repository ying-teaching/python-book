def fib(number):
    assert(number >= 0)  # should not happen

    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fib(number - 1) + fib(number - 2)


def efficient_fib(number):
    return round((((1 + 5 ** 0.5) / 2) ** number) / (5 ** 0.5))


if __name__ == '__main__':
    import sys

    argv = sys.argv
    if len(argv) > 1:
        n = int(argv[1])
    else:
        n = 7

    result = fib(n)
    # result = efficient_fib(n)
    print(f'fib({n}) is {result}')
