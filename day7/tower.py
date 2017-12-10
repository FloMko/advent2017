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
    leaf = False
    if '->' in instr:
        leaf = True
    name = instr.split()[0]
    weight = int(instr.split()[1].strip('()'))
    if leaf:
        leap = instr.split('-> ')[1].split(', ')
        return name, leaf, leap, weight
    else:
        return name, leaf, None, weight


def aknowleg(leaflist, aknowleged=set()):
    for prog in leaflist:
        aknowleged.add(prog)
    return(aknowleged)


def aknowleg_prog(programm, aknowleged_prog=set()):
    aknowleged_prog.add(programm)
    return(aknowleged_prog)


def buld_tower(inlist=indata()):
    tower = {}
    for line in inlist:
        name, leaf, leap, weight = chunk(line)
        tower[name] = weight, leaf, leap
    return tower


def balance(tower, name):
    root_weight = tower[name][1]
    leafs = tower[name][2]
    weight = 0
    if leafs is not None:
        for leaf in leafs:
            weight += tower[leaf][1]
    return root_weight >= weight


def root():
    aknowleged = set()
    aknowleged_prog = set()
    tower = buld_tower()
    for name in tower.keys():
        leap = tower[name][2]
        if leap is not None:
            aknowleged = aknowleg(leap, aknowleged)
        aknowleged_prog = aknowleg_prog(name, aknowleged_prog)
    for prog in aknowleged_prog:
        if prog not in aknowleged:
            return(prog)


def unbalance():
    aknowleged = set()
    aknowleged_prog = set()
    tower = buld_tower()
    for name in tower.keys():
        unbalance = balance(tower, name)


if __name__ == '__main__':
    unbalance()
