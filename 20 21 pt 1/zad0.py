import math


def check(n, digit):
    fact = math.factorial(n)
    while fact % 10 == 0:
        fact //= 10

    return fact % 10 == digit


def last_factorial_digit(n):
    factorial = 1

    for i in range(1, n + 1):
        while i % 10 == 0:
            i //= 10

        while factorial % 10 == 0:
            factorial //= 10

        digit_mask = 10
        while ((factorial % digit_mask) * (i % digit_mask)) % digit_mask == 0:
            digit_mask *= 10

        digit_mask *= 10

        factorial %= digit_mask
        i %= digit_mask
        factorial *= i

        # print("f({}) = {}".format(i, factorial))

    while factorial % 10 == 0:
        factorial //= 10

    return factorial % 10


for N in range(3000):
    last_digit = last_factorial_digit(N)
    if not check(N, last_digit):
        print("f({}) = {}".format(N, last_digit))
