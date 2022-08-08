# Bartłomiej Kozera
def f(x):
    low, high = 1, 1

    while low <= x:
        tmpLow = low
        tmpHigh = high

        while tmpHigh <= x:
            if x % tmpHigh == 0:
                if x / tmpHigh == low:
                    return True

            tmpLow, tmpHigh = tmpHigh, tmpLow + tmpHigh
        low, high = high, low + high

    return False
