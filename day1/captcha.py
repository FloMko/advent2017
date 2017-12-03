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

def striped():
    chain = input()
    ns = [int(i) for i in str(chain)]
    return ns
