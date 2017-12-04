import math

t = 289326
def findway(t=289326):
    """find hypotenuse"""
    n = math.ceil((math.sqrt(t)-1)/2)
    if t <= (2*n-1)**2 + 2*n:
        ind = t-(2*n-1)**2-n
    elif t <= (2*n-1)**2 + 4*n:
        ind = (2*n-1)**2 + 3*n - t
    elif t <= (2*n-1)**2 + 6*n:
        ind = (2*n-1)**2 + 5*n - t
    else:
        ind = t - (2*n-1)**2 - 7*n

    return abs(n) + abs(ind)


if __name__ == '__main__':
    findway()