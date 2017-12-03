def indata():
    """Just read and store"""
    intext =[] 
    with open('input.txt', 'r') as data:
        for line in data:
            intext.append(line.split('\t'))
    return(intext)

def middata(intext):
    """chunk an prepare to work"""
    midtext = []
    pureline = []
    for line in intext:
        lastelement = line.pop(-1).strip()
        line.append(lastelement)
        midtext.append(line)
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

def main():
    """general cinstruct"""
    midtext = middata(indata())
    return midtext

