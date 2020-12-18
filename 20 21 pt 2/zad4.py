#  Jakub Karbowski
"""
Funckja can_divide sprawdza czy mozna pociac liczbe na 2 czesci
tak ze pierwsza czesc jest liczba pierwsza a druga tez moze byc pocieta.
Dodatkowo liczy sie count pociec ktory tez musi byc pierwszy
"""


def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    div = 3
    while div * div <= n:
        if n % div == 0:
            return False
        div += 2
    return True


def divide(N):
    #  count to liczba fragmentow przed wywolaniem wiec start od 0
    def can_divide(N, count=0):
        if N < 10:  # juz nie podzieli
            #  pocielismy na 1 kawalek wiec count + 1
            return is_prime(N) and is_prime(count + 1)
        else:
            # pierwsze ciecie
            a, b = divmod(N, 10)
            i = 10  # pomaga w budowaniu liczy od tylu
            while a > 0:
                #  dodalismy jeden nowy kawalem wiec count + 1
                if is_prime(b) and can_divide(a, count + 1):
                    return True

                # przesuwamy punkt ciecia
                a, digit = divmod(a, 10)
                b += digit * i
                i *= 10

            # na koncu mamy cala liczbe w b to mozemy sprawdzic czy moze calosc dziala
            return is_prime(b) and is_prime(count + 1)

    return can_divide(N)


print(divide(22))
print(divide(273))  # True, podział 2|7|3
print(divide(22222))  # True, podział 2|2|2|2|2
print(divide(23672))  # True, podział 23|67|2
print(divide(2222))  # False
print(divide(21722))  # False
