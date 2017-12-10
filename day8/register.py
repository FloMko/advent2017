def indata():
    """Just read and store"""
    with open('input.txt', 'r') as data:
        instr = [line.strip() for line in data]
    return instr

def collect(inlist=indata()):
    regiester_dict = {}
    for line in inlist:
        regiester_dict[line.split()[0]] = 0
    return regiester_dict


if __name__ == '__main__' :
    main()
