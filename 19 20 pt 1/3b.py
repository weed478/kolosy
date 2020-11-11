def is_valid(placed, board):
    total_sum = board[0][placed[0]]
    for y in range(1, len(placed)):
        total_sum += board[y][placed[y]]
        if (placed[y - 1] - 1) <= placed[y] <= (placed[y - 1] + 1):
            return False

    return total_sum == 0


def tick_positions(placed, rollover):
    placed[len(placed) - 1] += 1
    for y in range(len(placed) - 2, -1, -1):
        if placed[y + 1] >= rollover:
            placed[y + 1] = 0
            placed[y] += 1
        else:
            break


def can_place(board):
    size = len(board)
    placed = [0] * size

    while placed[0] < size:
        if is_valid(placed, board):
            return True

        tick_positions(placed, size)

    return False


tab = [[1, 1, 2, 3, 4, 5, 6, 7],
       [1, 1, 2, 10, 4, 5, 6, 7],
       [2, 5, 2, 3, 4, 5, 6, 7],
       [3, 1, 2, 3, 5, 5, 6, 7],
       [4, 1, 2, 3, 4, 5, 20, 7],
       [5, 1, 2, 3, 20, 5, 6, 7],
       [6, 1, 3, 3, 4, 5, 6, 7],
       [7, 1, 2, 3, 123, 5, 6, 7]]

print(can_place(tab))

