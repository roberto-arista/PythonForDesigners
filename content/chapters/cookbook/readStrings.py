def readStringsFromFile(fileName):
    with open(fileName, mode='r', encoding='utf-8') as txtFile:
        return [ll.rstrip() for ll in txtFile.readlines()]


if __name__ == '__main__':
    words = readStringsFromFile('words.txt')
    # ['immediatamente', 'realmente', 'estremamente', 'solennemente', 'precedentemente', 'sicuramente', 'magnificamente', 'geneticamente', 'originariamente', 'seriamente', 'ingiustamente', 'ovviamente', 'sessualmente', 'particolarmente', 'indipendentemente']
