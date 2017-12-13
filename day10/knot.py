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
        inlist.rotate(-pos)
        original = list(inlist)
        rever = original[0:length]
        rever.reverse()
        for position in range(0, length):
            original[position] = rever[position]
        inlist = deque(original)
        inlist.rotate(pos)
        return inlist


if __name__ == '__main__':
    main()

