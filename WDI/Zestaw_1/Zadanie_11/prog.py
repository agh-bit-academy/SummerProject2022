# Kacper Słoniec

def f():
    def dziel(num):
        sum = 1
        i = 2
        while i**2 < num:
            if num%i == 0:
                sum += i + num//i
            i += 1
        if i*i == num:
            sum += i
        return sum

    for num in range (2, 10**6):
        sum = dziel(num)
        if num >= sum:
            continue
        sum2 = dziel(sum)
        if num == sum2:
            print(num, sum)