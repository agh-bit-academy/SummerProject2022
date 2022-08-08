# Dominik Adamczyk
# O(tabLen ^ 2)

def f(tab):
    maxLen = 0
    tabLen = len(tab)
    for i in range(0, tabLen):
        sumOfIndex = 0
        sumOfDigits = 0
        currLen = 0
        for j in range(i, tabLen):
            if j != i and tab[j - 1] >= tab[j]:
                break
            sumOfIndex += j
            sumOfDigits += tab[j]
            currLen += 1
            if sumOfDigits == sumOfIndex:
                maxLen = max(currLen, maxLen)

    return maxLen
