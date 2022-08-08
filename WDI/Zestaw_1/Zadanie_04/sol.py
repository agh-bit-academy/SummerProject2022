# Karol Sewiło
def f(number):
    sum_nr = 0
    i = 0
    while sum_nr < number:
        i += 1
        sum_nr += (2 * i) - 1
    if sum_nr == number:
        print(i)
    else:
        print(None)
