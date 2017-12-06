def indata():
    """Just read and store"""
    with open('input.txt', 'r') as data:
        instr = data.readline().split()
        instr = [int(bank) for bank in instr]
    return instr

def maxfind(intext):
    return max(intext), intext.index(max(intext))
def main():
    return indata()
    
if __name__ == '__main__':
    main()

