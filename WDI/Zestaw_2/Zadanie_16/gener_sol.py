# Paweł Konopka

import os


LIMIT = 1_000_000

def f(mx):
    if mx <= LIMIT:
        __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

        file = open(os.path.join(__location__, "sol.txt"), 'r')

        for line in file:
            akt = int(line)
            if akt >= mx:
                break
            print(akt)
