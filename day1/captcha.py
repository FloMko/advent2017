
def output():
    with open('input.txt', 'r') as data:
       intext = data.readline().strip()
    return(int(intext))
