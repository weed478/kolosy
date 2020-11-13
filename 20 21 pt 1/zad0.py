def last_factorial_digit(n):
    factorial = 1

    for i in range(1, n + 1):
        factorial *= i
        while factorial % 10 == 0:
            factorial //= 10

        what = 10
        while ((factorial % what) * (i + 1)) % what == 0:
            what *= 10

        factorial = factorial % (what * 10)

        print("f({}) = {}".format(i, factorial))

    return factorial % 10


N = 30000
print("f({}) = {}".format(N, last_factorial_digit(N)))
