# Maciej Sieniek
def f(T, k):
    n = len(T)
    dic = {'UL': (-1, 1), 'UR': (1, 1), 'DL': (-1, -1), 'DR': (1, -1)}
    for i in range(1, n // 2):
        for a in range(i, n - i):
            for b in range(i, n - i):
                corner_sum = 0
                for el in dic:
                    corner_sum += T[a + dic[el][0]][b + dic[el][1]]
                print(T[a][b], corner_sum)
                if corner_sum == k:
                    return True, a, b
    return False
