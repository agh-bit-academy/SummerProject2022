# Szymon Rusiecki
from random import randint


def f(n):
    twoInSameDay = 0
    notInSameDay = 0
    dayInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for _ in range(10 ** 5):
        people = [[randint(0, 11), None] for _ in range(n)]
        for j in range(n):
            people[j][1] = randint(0, dayInMonth[people[j][0]] - 1)

        flag = False
        for j in range(n):
            for k in range(j + 1, n):
                if people[j] == people[k]:
                    flag = True
                    break

        if flag:
            twoInSameDay += 1
        else:
            notInSameDay += 1

    return twoInSameDay / (twoInSameDay + notInSameDay)
