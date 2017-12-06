def indata():
    """Just read and store"""
    with open('input.txt', 'r') as data:
        instr = data.readline().split()
    return instr


def turn(inlist, i=0, j=0, val=0):
    while i < len(inlist) :
        j +=1
        inlist[i] += 1
        i += inlist[i] -1
    return j

def main():
    step = turn(indata())
    return step
    print(step)


if __name__ == '__main__':
    main()

