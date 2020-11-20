# Jakub Karbowski
"""
Probujemy wszystkie podciagi dlugosci 1 do len / 2 + 1.
Przechodzimy przez reszte napisu sprawdzajac cyklicznosc znakow
Szukamy najdluzszego
"""


def multi(T):
    max_len = 0

    for text in T:
        for i in range(1, len(text) // 2 + 1):
            if len(text) % i != 0:
                # wtedy na pewno nie bedzie wielokrotny
                continue

            # patrzymy czy reszta to powtorzenie pierwszego
            for j in range(i, len(text)):
                if text[j] != text[j % i]:
                    break
            else:
                if len(text) > max_len:
                    max_len = len(text)
                    break

    return max_len


t = [
    "AAAA",
    "AAAABAAAAB",
    "ABCABA",
    "BDACBDACBDAC"
]

print(multi(t))
