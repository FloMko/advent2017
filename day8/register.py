def indata():
    """Just read and store"""
    with open('input.txt', 'r') as data:
        instr = [line.strip() for line in data]
    return instr

if __name__ == '__main__' :
    main()
