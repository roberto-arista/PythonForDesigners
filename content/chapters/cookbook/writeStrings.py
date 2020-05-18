def writeStringsToFile(fileName, strings):
    with open(fileName, mode='w', encoding='utf-8') as txtFile:
        for eachStr in strings:
            txtFile.write(f'{eachStr}\n')


if __name__ == '__main__':
    words = ['immediatamente', 'realmente', 'estremamente', 'solennemente', 'precedentemente', 'sicuramente', 'magnificamente', 'geneticamente', 'originariamente', 'seriamente', 'ingiustamente', 'ovviamente', 'sessualmente', 'particolarmente', 'indipendentemente']
    writeStringsToFile('words.txt', words)
