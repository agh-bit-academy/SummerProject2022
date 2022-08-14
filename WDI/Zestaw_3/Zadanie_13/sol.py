# Dominik Adamczyk
def f(tab):
    reverse = tab[::-1]
    tab_len = len(tab)
    max_len = 0
    for i in range(tab_len):
        for j in range(tab_len):
            i_cp = i
            curr_len = 0
            while i_cp < tab_len and j < tab_len and tab[i_cp] == reverse[j]:
                curr_len += 1
                i_cp += 1
                j += 1
            max_len = max(max_len, curr_len)
    return max_len
