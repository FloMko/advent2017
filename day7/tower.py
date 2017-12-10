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
        return name, leaf, [], weight


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
        if unbalance is not True:
            leap = tower[name][2]
            if leap is not None:
                aknowleged = aknowleg(leap, aknowleged)
            aknowleged_prog = aknowleg_prog(name, aknowleged_prog)
            for prog in aknowleged_prog:
                if prog in aknowleged:
                    print(prog)

def _weight(root, tower):
    """Recursively determine the weight of root and its leaf nodes"""
    weight, leap, leaves = tower[root]
    weights = []
    for leaf in leaves:
        w, _ = _weight(leaf, tower)
        weights.append(w)
    return weight + sum(weights), weights


def part2(root, tower):
    prev_weight = 0
    while True:
        root_weight, leap, leaf_nodes = tower[root]
        # Compute weight of root and it's leaves
        weight, leaf_weights = _weight(root, tower)

        # Check if there's a leaf node with wrong weight
        unique_weights = set(leaf_weights)
        if len(unique_weights) > 1:
            # Find the wrong leaf node
            dupes = set(w for w in leaf_weights if leaf_weights.count(w) > 1)
            wrong = (unique_weights - dupes).pop()  # always len == 1 here
            # Update root and prev_weight for next iteration
            root = leaf_nodes[leaf_weights.index(wrong)]
            prev_weight = dupes.pop()
        else:
            # All leaf nodes have same weight, the problem is root
            w = prev_weight - sum(leaf_weights)
            return (root, w)

    raise Exception('Something went wrong!')

def main():
    rootl = root()
    tower = buld_tower()
    print(part2(rootl, tower))


if __name__ == '__main__':
    main()
