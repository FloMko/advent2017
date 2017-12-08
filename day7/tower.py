def indata():
    """Just read and store"""
    with open('input.txt', 'r') as data:
        instr = data.readline().split()
        instr = [int(bank) for bank in instr]
    return instr

    
if __name__ == '__main__':
    main()

