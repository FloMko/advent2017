def input():
    """Just read and store"""
    with open('input.txt', 'r') as data:
        phrases = [line.split() for line in data.readlines()]
    return phrases

if __name__ == '__main__':
    main()
