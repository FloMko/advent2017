def indata():
    """Just read and store"""
    with open('input.txt', 'r') as data:
       intext = data.readline()
    return(intext)

