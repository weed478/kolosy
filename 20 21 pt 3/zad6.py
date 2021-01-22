# Jakub Karbowski
"""
Bierzemy kolejne z z1 i przesuwamy sie w z2, z3 patrzac czy tez wystepuje
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def iloczyn(z1, z2, z3):
    if z1 is None or z2 is None or z3 is None:
        return None

    wart = Node(None)
    common = wart

    # wartowniki
    zb1 = Node(None)
    zb1.next = z1

    zb2 = Node(None)
    zb2.next = z2

    zb3 = Node(None)
    zb3.next = z3

    q1 = zb1
    p1 = q1.next

    q2 = zb2
    p2 = q2.next

    q3 = zb3
    p3 = q3.next

    while p1 is not None:
        # gonimy drugim
        while p2 is not None and p2.val < p1.val:
            q2 = p2
            p2 = p2.next

        if p2 is None or p2.val > p1.val:
            # p1.val nie ma w z2
            q1 = p1
            p1 = p1.next
            continue

        # p2.val == p1.val

        # gonimy trzecim
        while p3 is not None and p3.val < p1.val:
            q3 = p3
            p3 = p3.next

        if p3 is None or p3.val > p1.val:
            # p1.val nie ma w z3
            q1 = p1
            p1 = p1.next
            continue

        # p3.val == p1.val
        # p1, p2, p3 ustawione na elemencie wspolnym
        # przepinamy
        wart.next = p1
        wart = wart.next
        # usuwamy
        q1.next = p1.next
        wart.next = None

        # przesuwamy p1
        p1 = q1.next

    return common.next


t1 = Node(1)
t1.next = Node(2)
t1.next.next = Node(3)

t2 = Node(-1)
t2.next = Node(0)
t2.next.next = Node(1)
t2.next.next.next = Node(2)
t2.next.next.next.next = Node(3)
t2.next.next.next.next.next = Node(6)

t3 = Node(-5)
t3.next = Node(1)
t3.next.next = Node(2)
t3.next.next.next = Node(3)
t3.next.next.next.next = Node(5)
t3.next.next.next.next.next = Node(10)
t3.next.next.next.next.next.next = Node(11)

t = iloczyn(t1, t2, t3)
while t is not None:
    print(t.val)
    t = t.next
