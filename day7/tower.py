def indata():
    """Just read and store"""
    with open('input.txt', 'r') as data:
        instr = [line.strip() for line in data]
#        instr = [graph for graph in instr]
    return instr

def chunk(instr):
    """prepare record to analyze
       return name, posithion and state
       of child, True if have
    """
    name = ''
    pos = int()
    leaf = False
    if '->' in instr:
        leaf = True
    name = instr.split()[0]



if __name__ == '__main__':
    main()

