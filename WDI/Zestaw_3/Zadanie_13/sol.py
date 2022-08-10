# Dominik Adamczyk

def f(tab: list) -> int:  # O(n ^ 2) - Rozwiązane programowaniem dynamicznym (II sem), na WDI powinno wystarczyć f2
    tabLen = len(tab)
    DP = [[0 for _ in range(tabLen)] for _ in range(tabLen)]
    ans = 1
    for i in range(tabLen):
        for j in range(tabLen):
            if (i == 0 or j == 0) and tab[i] == tab[- (j + 1)]:
                DP[i][j] = 1
            elif tab[i] == tab[- (j + 1)]:
                DP[i][j] = DP[i - 1][j - 1] + 1
                ans = max(ans, DP[i][j])
    return ans


def f2(tab: list) -> int:  # O(n ^ 3)
    reverse = tab[::-1]
    tabLen = len(tab)
    maxLen = 0
    for i in range(tabLen):
        for j in range(tabLen):
            iCpy = i
            currLen = 0
            while iCpy < tabLen and j < tabLen and tab[iCpy] == reverse[j]:
                currLen += 1
                iCpy += 1
                j += 1
            maxLen = max(maxLen, currLen)
    return maxLen
