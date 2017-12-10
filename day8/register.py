import operator

def indata():
    """Just read and store"""
    with open('input.txt', 'r') as data:
        instr = [line.strip() for line in data]
    return instr


def collect(inlist=indata()):
    regiester_dict = {}
    for line in inlist:
        regiester_dict[line.split()[0]] = 0
    return regiester_dict

def main():
    opr = {"<":operator.lt,"<=":operator.le,"==": operator.eq,"!=" :operator.ne,">=": operator.ge, ">":operator.gt}
    variables = collect()
    file = indata()
    top = 0
    modified = 0
    for line in file:
        variable, change, amount, _, check, op, base = line.split()
        if opr[op](variables[check], int(base)):
            if change == 'inc':
                variables[variable] += int(amount)
            else:
                variables[variable] -=int(amount)
            if top < variables[variable]:
                top = variables[variable]
    print("result max:", variables[max(variables.keys(), key=lambda key:variables[key])])
    print("Max amount: ", top)

if __name__ == '__main__':
    main()
