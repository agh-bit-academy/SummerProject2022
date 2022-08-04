# Karol Sewiło
def f(number):
    sumNr = 0
    i = 0
    while sumNr < number:
        i += 1
        sumNr += 2*i - 1
    if sumNr == number:
        print(i)
        return
    else:
        print(None)
