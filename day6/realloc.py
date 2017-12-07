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
        return True

def distribute(intext, i, n):
    """redistrib memory
       take state memory bank, index val ,max value 
       return modified memory bank, 
    """
    z = i
    while n > 0:
        i = (i + 1) % len(intext)
        print(type(intext[i]))
        intext[i] += 1
        n -= 1
    intext[z] = 0
    return intext

def main(not_find_yet=False):
    memory = indata()
#    while not_find_yet:
#       not_find_yet = detect(memory,aknowleged)
#       val, pos = realloc.maxfind(memory)


    return indata()
    
if __name__ == '__main__':
    main()

