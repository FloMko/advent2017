def indata():
    """Just read and store"""
    with open('input.txt', 'r') as data:
        instr = [line.strip() for line in data]
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
    ## should find method to convert string
    ## with parentheses to int, or not to conver
    return name, leaf

def aknowleg(leaflist, aknowleged=set()):
    for prog in leaflist:
        aknowleged.add(prog)
    return(aknowleged)


if __name__ == '__main__':
    main()

