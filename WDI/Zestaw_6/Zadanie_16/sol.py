# Izabella Rosikoń
def waga(s):
    samogloski = "aeiouy"
    asc = 0
    sam = 0
    for char in s:
        asc += ord(char)
        if char in samogloski:
            sam += 1
    return asc, sam


def f(s1, s2, p="", i=0):
    if waga(p) == waga(s1):
        return
    if i == len(s2):
        return
    f(s1, s2, p, i + 1)
    f(s1, s2, p + s2[i], i + 1)
