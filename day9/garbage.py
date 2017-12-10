import re

garbage = 0

def indata():
    """Just read and store"""
    with open('input.txt', 'r') as data:
        instr = data.readline()
    return instr

def rewrite(instr=indata()):
    new_str = re.sub('!.','',instr)
    return re.sub('<.*?>', count, new_str)

def count(match):
    global garbage
    start, end = match.span()
    garbage += end - start - 2  # -2 since we need to account for <>
    return ''

def score(instr=indata()):
    scor = 0
    depth = 0
    for symbol in rewrite(instr):
        if symbol == '{':
            depth +=1
        elif symbol == '}':
            scor += depth
            depth -=1
    return scor

def main():
    print(score())
    print(garbage)

if __name__ == '__main__':
    main()
