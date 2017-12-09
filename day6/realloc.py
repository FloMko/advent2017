def indata():
    """Just read and store"""
    with open('input.txt', 'r') as data:
        instr = data.readline().split()
        instr = [int(bank) for bank in instr]
    return instr


def maxfind(intext):
    return max(intext), intext.index(max(intext))


def detect(intext, aknowleged):
    if intext in aknowleged:
        return False


def aknowleg(intext, aknowleged=[]):
    aknowleged.append(intext)
    return aknowleged


def distribute(intext, i, n):
    """redistrib memory
    take state memory bank, index val ,max value 
    return modified memory bank, 
    """
    z = i
    while n > 0:
        i = (i + 1) % len(intext)
        intext[i] += 1
        n -= 1
    intext[z] = 0
    return intext


def stepcount(memory, not_find_yet=True):
    aknowleged = []
    step = 0
    while not_find_yet:
        not_find_yet = detect(memory, aknowleged)
        aknowleged = aknowleg(memory, aknowleged)
        val, pos = maxfind(memory)
        memory = distribute(memory, pos, val)
        step += 1
    return step


def main(not_find_yet=True):
    memory = indata()
    aknowleged = []
    step = 0
    while not_find_yet:
        aknowleged = aknowleg(memory, aknowleged)
        not_find_yet = detect(memory, aknowleged)
        val, pos = maxfind(memory)
        memory = distribute(memory, pos, val)
        step += 1
    return step


if __name__ == '__main__':
    main()
