from random import randint

class Node():
    rfll_seed = 0

    def __init__(self, val=None):
        self.key = val
        self.next = None

    @staticmethod
    def gen_two_random(
        size: int, l_range: int, r_range: int,
        rand_gen=randint
    ):
        head_A = Node(None)
        head_B = Node(None)
        tail_A = head_A
        tail_B = head_B
        for _ in range(size):
            val = rand_gen(l_range, r_range)
            tail_A.next = Node(val)
            tail_B.next = Node(val)
            tail_A = tail_A.next
            tail_B = tail_B.next

        return head_A, head_B

    def __eq__(A, B):
        if not type(A) == Node or not type(B) == Node:
            return False

        if A.key == None:
            A = A.next
        if B.key == None:
            B = B.next

        while A and B:
            if A.key != B.key:
                return False
            A = A.next
            B = B.next

        if A or B:
            return False

        return True
