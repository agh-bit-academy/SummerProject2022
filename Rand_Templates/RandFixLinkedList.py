from random import randint

class Node():
    rfll_seed = 0

    def __init__(self, val):
        self.key = val
        self.next = None

    @staticmethod
    def gen_random(
        size: int, l_range: int, r_range: int,
        rand_gen=randint
    ):
        head = Node(None)
        tail = head
        for _ in range(size):
            tail.next = Node(rand_gen(l_range, r_range))
            tail = tail.next

        return head
