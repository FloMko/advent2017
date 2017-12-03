from functools import reduce
from fractions import gcd

maxf = 0
minf = 9999
checks = 0

def indata():
    """Just read and store"""
    intext =[] 
    with open('input.txt', 'r') as data:
        for line in data:
            intext.append(line.split())
    return(intext)

def middata(intext):
    """conver str to int"""
    midtext = []
    for line in intext:
        row = [int(s) for s in line]
        midtext.append(row)
    return midtext


def maxof(inline):
    """How to find max value"""
    maxf = 0
    for value in inline:
        if int(value) > maxf:
            maxf = int(value)
    return maxf

def minof(inline):
    """How to find min value"""
    minf = 9999
    for value in inline:
        if int(value) < minf:
            minf = int(value)
    return minf

def work(inline):
    maxf = maxof(inline)
    minf = minof(inline)
    diff = maxf - minf
    return diff

def pairwork(inline):
    for i in inline:
        for j in inline:
            if i == j:
                continue
            if j == 0:
                continue
            if i % j == 0:
                return i // j
    return 0

def main():
    """general construct"""
    midtext = middata(indata())
    print(sum(map(pairwork, midtext)))
    return sum(map(pairwork, midtext))

if __name__ == '__main__':
    main()

