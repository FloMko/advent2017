
def indata():
    """Just read and store"""
    with open('input.txt', 'r') as data:
        instr = data.readline().split()
    return instr

def reverse(inlist, pos, length):
        """
        get circular list, position in list and lenght of reverse
        return modified list
        """
        rever = inlist[pos:length]
        rever.reverse()
        for position in range(pos, pos +  length):
            inlist[position] = rever[position - length]
        return inlist

if __name__ == '__main__':
    main()

