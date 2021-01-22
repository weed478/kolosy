# Jakub Karbowski
"""
Generujemy (N po 3) zbiorow i liczymy NWD.
Ale testy sa zle!
nwd(2, 4, 7) == 1
"""


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def multi_gcd(t):
    # liczymy nwd wielu liczb liczac ndw poprzedniego nwd z kolejna liczba
    divisor = t[0]
    for i in t[1:]:
        divisor = gcd(divisor, i)
    return divisor


def trojki(T):
    n = len(T)
    count = 0
    # pierwsza petla zostawia 2 elementy na koncu
    for t1 in range(n - 2):
        # druga sprawdza tylko 2 kolejne elementy
        for t2 in range(t1 + 1, t1 + 3):
            # trzecia jeszcze 2 kolejne
            for t3 in range(t2 + 1, min(t2 + 3, n)):
                if multi_gcd([T[t1], T[t2], T[t3]]) == 1:
                    # print(T[t1], T[t2], T[t3])
                    count += 1

    return count


print(trojki([2,4,6,7,8,10,12])) # 0 trójek
print(trojki([2,3,4,6,7,8,10])) # 1 trójka (3,4,7)
print(trojki([2,4,3,6,5])) # 2 trójki (2,3,5),(4,3,5)
print(trojki([2,3,4,5,6,8,7])) # 5 trójek (2,3,5),(3,4,5),(3,5,8),(5,6,7),(5,8,7)
