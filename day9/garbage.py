import re

def indata():
    """Just read and store"""
    with open('input.txt', 'r') as data:
        instr = data.readline()
    return instr

def rewrite(instr=indata()):
    new_str = re.sub('!.','',instr)
    return re.sub('<.*?>', '<>', new_str)


if __name__ == '__main__':
    main()
