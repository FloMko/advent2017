def input():
    """Just read and store"""
    with open('input.txt', 'r') as data:
        instr = [line.split() for line in data.readlines()]
    return instr

def change(list_instr, i=0, j=0):
    while i <= len(list_instr)- 1:
        temp = list_instr[i]
        list_instr[i] +=1
        i += temp
        j+=1

    return list_instr

if __name__ == '__main__':
    main()
