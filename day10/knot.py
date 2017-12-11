from collections import deque

def indata():
    """Just read and store"""
    with open('input.txt', 'r') as data:
        instr = deque(data.readline().split())
    return instr

def reverse(inlist, pos, length):
        """
        get circular list, position in list and lenght of reverse
        return modified list
        """
        rever = collections.deque(inlist)
        rever.rotate(-pos)
        for position in range(pos, pos +  length % len(inlist)):
            inlist[position % len(inlist)] = rever[position - length % len(inlist)]

        return inlist

if __name__ == '__main__':
    main()

