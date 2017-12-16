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

def simple_knot(seq, sault, repeat=1):
    pos = 0
    skip_size = 0
    for length in sault*repeat:
        seq = reverse(seq, pos, length)
        pos = pos + length + skip_size
        skip_size+=1
    return seq

def xor(sparse_hash):
    xored = 0
    for n in sparse_hash:
        xored ^= n
    return xored


def complicated_knot(seq, sault):
    sault = [ord(str(c)) for c in sault]
    lengths.extend([17, 31, 73, 47, 23])
    dense_hash = [0]*16
    res = simple_knot(list_[:], lengths, times=64)
    dense = [0]*16
    for i in range(16):
        dense[i] = xor(res[i*16:i*16+16])
    return ''.join(['%02x' % d for d in dense])

def main():
    sault=indata()
    seq = [seq for seq in range(0,256)]
    p1 = simple_knot(seq[:], sault)
    print(p1[0] * p1[1])
    print(complicated_knot(seq[:], sault))



if __name__ == '__main__':
    main()

