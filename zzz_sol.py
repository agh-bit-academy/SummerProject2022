# Szymon Rusiecki
from random import randint


def f(N):
    two_in_same_day = 0
    not_in_same_day = 0
    dayInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for _ in range(10 ** 5):
        people = [[randint(0, 11), None] for _ in range(N)]
        for j in range(N):
            people[j][1] = randint(0, dayInMonth[people[j][0]] - 1)

        flag = False
        for j in range(N):
            for k in range(j + 1, N):
                if people[j] == people[k]:
                    flag = True
                    break

        if flag:
            two_in_same_day += 1
        else: 
            not_in_same_day += 1

    print(two_in_same_day / (two_in_same_day + not_in_same_day))

f(20)