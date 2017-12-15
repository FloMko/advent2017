from collections import deque

def indata():
    """Just read and store"""
    with open('input.txt', 'r') as data:
        instr = [int(data) for data in data.readline().strip().split(',')]
    return instr

def reverse(inlist, pos, length):
    """
    get circular list, position in list and lenght of reverse
    return modified list
    """
    inlist = deque(inlist)
    inlist.rotate(-pos)
    original = list(inlist)
    rever = original[0:length]
    rever.reverse()
    for position in range(0, length):
        original[position] = rever[position]
    inlist = deque(original)
    inlist.rotate(pos)
    return inlist

def main():
    sault=indata()
    pos = 0
    skip_size = 0
    seq = [seq for seq in range(0,256)]
    for length in sault:
        seq = reverse(seq, pos, length)
        pos = pos + length + skip_size
        skip_size+=1
    return seq

def xor(sparse_hash):
    xored = 0
    for n in sparse_hash:
        xored ^= n
    return xored


def main2():
    sault=indata()
    sault+=[17, 31, 73, 47, 23]
    


if __name__ == '__main__':
    main()

