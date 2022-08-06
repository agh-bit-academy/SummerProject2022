# Szczepan Rzeszutek
def f():
    def function(x):
        return x ** x - 2022

    a, b = 0, 100
    while abs(a - b) > 10 ** (-6):
        x = (a + b) / 2
        if function(x) == 0:
            print(x)
        if function(a) * function(x) < 0:
            b = x
        elif function(x) * function(b) < 0:
            a = x

    print((a + b) / 2)
