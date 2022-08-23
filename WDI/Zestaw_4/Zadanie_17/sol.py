# Dominik Adamczyk

def f(A):
    xlen = len(A[0])
    ylen = len(A)
    coords = (0, 0)
    maxsum = 0
    for y in range(ylen):
        for x in range(xlen):
            currsum = 0
            if x != 0:
                if y != 0:
                    currsum += A[y - 1][x - 1]
                if y != ylen - 1:
                    currsum += A[y + 1][x - 1]
                currsum += A[y][x - 1]
            if x != xlen - 1:
                if y != 0:
                    currsum += A[y - 1][x + 1]
                if y != ylen - 1:
                    currsum += A[y + 1][x + 1]
                currsum += A[y][x + 1]
            if y != 0:
                currsum += A[y - 1][x]
            if y != ylen - 1:
                currsum += A[y + 1][x]
            if currsum > maxsum:
                maxsum = currsum
                coords = (x, y)
    return coords
