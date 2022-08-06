def decimalToBinary(number):
    k = 0
    decimalNr = 0
    while number > 0:
        decimalNr += (number % 2) * (10 ** k)
        k += 1
        number //= 2
    return decimalNr


def countIfCanBeDivided(number, bitMask, divisor, length):
    newNumber = 0
    k = 0
    for _ in range(length):
        if bitMask % 10 == 1:
            newNumber += (number % 10) * (10 ** k)
            k += 1
        bitMask //= 10
        number //= 10
    if newNumber % divisor == 0:
        return 1
    else:
        return 0


def f(number, divisor):

    if number == 0:
        print(1)
        return

    number = abs(number)
    divisor = abs(divisor)
    tempNumber = number
    length = 0
    counter = 0

    while tempNumber > 0:
        length += 1
        tempNumber //= 10

    for i in range(1, 2**length):
        counter += countIfCanBeDivided(number, decimalToBinary(i), divisor, length)
    print(counter)
