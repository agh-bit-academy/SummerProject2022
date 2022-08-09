# Dominik Adamczyk
# Rozwiązania do optymalizacji testów

def f(tab: list) -> int:  # O(n)
    tabLen = len(tab)
    if tabLen == 1:
        return 1
    length = 1
    maxLen = 2
    diff = tab[0] - tab[1]

    for i in range(1, tabLen):
        if tab[i - 1] - tab[i] == diff:
            length += 1
            maxLen = max(length, maxLen)
        else:
            length = 2
            diff = tab[i - 1] - tab[i]
    return maxLen


def f2(tab: list) -> int:  # O(n ^ 2)
    tabLen = len(tab)
    if tabLen == 1:
        return 1
    maxLen = 2
    for i in range(tabLen - 1):
        diff = tab[i] - tab[i + 1]
        leng = 1
        for j in range(i + 1, tabLen):
            if tab[j - 1] - tab[j] == diff:
                leng += 1
            else:
                break
        maxLen = max(maxLen, leng)
    return maxLen
