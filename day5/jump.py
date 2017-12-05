def indata():
    """Just read and store"""
    with open('input.txt', 'r') as data:
        instr = [line.split() for line in data.readlines()]
    return instr

def change(list_instr, i=0):
    list_instr[i] +=1
    return (list_instr, list_instr[i+1])


def main():
    inlist = indata()
    while i <= len(indata) -1 :
        inlist, i = change(inlist, i)
        j = j + 1
        return j

if __name__ == '__main__':
    main()