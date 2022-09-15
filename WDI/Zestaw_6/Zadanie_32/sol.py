# Izabella Rosikoń
def f(T, k):
    def rec(T, k, sum_1, sum_2, elements_1, elements_2, i):
        if sum_1 == sum_2 and elements_1 + elements_2 == k:
            return True
        if i == len(T) - 1:
            return False
        a = rec(T, k, sum_1 + T[i], sum_2, elements_1 + 1, elements_2, i + 1)
        b = rec(T, k, sum_1, sum_2 + T[i], elements_1, elements_2 + 1, i + 1)
        c = rec(T, k, sum_1, sum_2, elements_1, elements_2, i + 1)
        return a or b or c
    return rec(T, k, 0, 0, 0, 0, 0)
