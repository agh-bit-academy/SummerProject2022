# Krzysztof Mach


def f(num):
    a, b = 1, 1
    while a <= num:
        temp_a, temp_b = a, b

        while temp_b <= num:
            if a * temp_b == num:
                return True
            temp_a, temp_b = temp_b, temp_a + temp_b

        a, b = b, a + b
    return False
