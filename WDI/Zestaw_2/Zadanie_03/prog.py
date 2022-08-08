# Bartłomiej Kozera
def f(num):
    pal_dec, pal_bin = False, False
    num_as_str = str(num)
    if num_as_str == num_as_str[::-1]:
        pal_dec = True

    num_bin = bin(num)[2:]
    if num_bin == num_bin[::-1]:
        pal_bin = True

    return (pal_dec, pal_bin)
