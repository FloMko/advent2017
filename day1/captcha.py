def input():
    """Just read and store"""
    with open('input.txt', 'r') as data:
       intext = data.readline().strip()
    return(intext)

def output():
    """Just read and return capcha"""
    with open('input.txt', 'r') as data:
       intext = data.readline().strip()
    return(work(intext))

def work(chain):
    sum = 0
    if chain[0] == chain[-1]:
        sum += int(chain[0])
    return sum

def striped(indata):
    ns = [int(i) for i in str(indata)]
    return ns

def filter(ns, predicate):
    filtered = []
    i = 0
    for i in range(len(ns)):
        if predicate(i, ns):
            filtered.append(ns[i])
        i += 1
    return sum(filtered)

def predicate1(i, ns):
    return ns[i] == ns[(i+1) % len(ns)]


def main():
    indata = input()
    ns = striped(indata)
    return filter(ns, predicate1)
     

    
if __name__ == '__main__':
    main()
