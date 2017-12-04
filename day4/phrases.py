def input():
    """Just read and store"""
    with open('input.txt', 'r') as data:
        phrases = [line.split() for line in data.readlines()]
    return phrases

def main():
    phrases = input()
    return sum(len(phrase) == len(set(phrase)) for phrase in phrases)

def main2():
    phrases = input()
    return sum(len(phrase) == len(set([tuple(word) for word in phrase])) for phrase in phrases)
if __name__ == '__main__':
    main()