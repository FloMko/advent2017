def indata():
    """Just read and store"""
    with open('input.txt', 'r') as data:
        instr = [int(bank) for bank in data.readline().split()]
    return instr

def maxfind(intext):
    return max(intext), intext.index(max(intext))

def detect(intext, aknowleged):
    if intext in aknowleged:
        return False
    else:
        return True

def loop(memory):
    step=1
    original = memory.copy()
    distribute(memory)
    while original != memory:
        step+=1
        distribute(memory)
    return step

def aknowleg(intext, aknowleged):
    aknowleged.append(intext)
    print(intext,aknowleged)
    return aknowleged

#def distribute(intext):
#    """redistrib memory
#    take state memory bank, index val ,max value 
#    return modified memory bank, 
#    """
#    n = max(intext)
#    i = intext.index(n)
#    intext[i] = 0
#    while n > 0:
#        i = (i + 1) % len(intext)
#        intext[i] += 1
#        n -= 1
#    return intext


def distribute(intext):
    n = max(intext)
    i = intext.index(n)
    intext[i] = 0
    while n > 0:
        i += 1
        if i >= len(intext):
            i = 0
        intext[i] += 1
        n -= 1


def stepcount(memory):
    aknowleged = set()
    step = 0
    while str(memory) not in aknowleged:
        step += 1
        aknowleged.add(str(memory))
        distribute(memory)
    return step
    print(step)

if __name__ == '__main__':
    step = loop(indata())
    print(step)
