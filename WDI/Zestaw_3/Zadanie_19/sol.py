# Dominik Adamczyk
def f(tab):
    max_len = 0
    tab_len = len(tab)
    for i in range(0, tab_len):
        sum_of_index = 0
        sum_of_digits = 0
        curr_len = 0
        for j in range(i, tab_len):
            if j != i and tab[j - 1] >= tab[j]:
                break
            sum_of_index += j
            sum_of_digits += tab[j]
            curr_len += 1
            if sum_of_digits == sum_of_index:
                max_len = max(curr_len, max_len)

    return max_len
