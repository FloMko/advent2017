
def indata():
    """Just read and store"""
    with open('input.txt', 'r') as data:
        instr = data.readline().split()
    return instr


if __name__ == '__main__':
    main()

