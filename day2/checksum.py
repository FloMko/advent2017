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


def max():
    """How to find max value"""

def min():
    """How to find min value"""

def main():
    """general cinstruct"""
    midtext = middata(indata())
    return midtext

