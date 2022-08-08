# Bartłomiej Kozera
def f(x):
    low, high = 1, 1

    while low <= x:
        temp_low = low
        tmp_high = high

        while tmp_high <= x:
            if x % tmp_high == 0:
                if x / tmp_high == low:
                    return True

            temp_low, tmp_high = tmp_high, temp_low + tmp_high
        low, high = high, low + high

    return False
