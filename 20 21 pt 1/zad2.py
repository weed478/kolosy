# Jakub Karbowski
"""
Najwieksza roznica bedzie pomiedzy najwieksza liczba a najmniejsza.
Przechodzimy przez tablice, porownujemy binarnie rzad z dotychczas min, max i szukamy min, max
"""


def row_gt(r1, r2):
    for i in range(len(r1)):
        if r1[i] == 1 and r2[i] == 0:
            return True
        elif r1[i] != r2[i]:
            return False

    return False


def row_lt(r1, r2):
    for i in range(len(r1)):
        if r1[i] == 0 and r2[i] == 1:
            return True
        elif r1[i] != r2[i]:
            return False

    return False


def distance(T):
    min_row = 0
    max_row = 0

    for row in range(1, len(T)):
        if row_gt(T[row], T[max_row]):
            max_row = row

        elif row_lt(T[row], T[min_row]):
            min_row = row

    return abs(max_row - min_row)




