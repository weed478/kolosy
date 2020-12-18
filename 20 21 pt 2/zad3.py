# Jakub Karbowski
"""
Wybieramy 2 po n*n pozycji i liczymy dla kazdej sume zaszachowanych pol.
Nie wiem czemu nie dziala :(
"""


def sum_row(tab, row):
    return sum(tab[row])


def sum_col(tab, col):
    return sum([row[col] for row in tab])


def chess(T):
    n = len(T)

    rows = [sum_row(T, r) for r in range(n)]
    cols = [sum_col(T, c) for c in range(n)]

    best_pos = None
    best_sum = None

    for i1 in range(n * n - 1):
        for i2 in range(i1 + 1, n * n):
            y1, x1 = divmod(i1, n)
            y2, x2 = divmod(i2, n)

            if x1 == x2:  # y1 != y2
                s = rows[y1] - T[y1][x1] + rows[y2] - T[y2][x2] + cols[x1] - T[y1][x1] - T[y2][x2]
            elif y1 == y2:  # x1 != x2
                s = cols[x1] - T[y1][x1] + cols[x2] - T[y2][x2] + rows[y1] - T[y1][x1] - T[y2][x2]
            else:  # x1, y1 != x2, y2
                s = cols[x1] + cols[x2] + rows[y1] + rows[y2] - T[y1][x2] - T[y2][x1] - 2 * T[y1][x1] - 2 * T[y2][x2]

            if best_sum is None or s > best_sum:
                best_sum = s
                best_pos = (y1, x1, y2, x2)

    return best_pos


print(chess([[4, 0, 2], [3, 0, 0], [6, 5, 3]]))
print(chess([[1, 1, 2, 3], [-1, 3, -1, 4], [4, 1, 5, 4], [5, 0, 3, 6]]))
