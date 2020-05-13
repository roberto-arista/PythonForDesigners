import csv

def loadTable(filePath, delimiter, quotechar):
    with open(filePath, mode='r', encoding='utf-8') as csvFile:
        tableReader = csv.reader(csvFile, delimiter=delimiter, quotechar=quotechar)
        return list(tableReader)


if __name__ == '__main__':
    table = loadTable('table.csv', '\t', '|')
    # [['city', 'country'], ['Shanghai', 'China'], ['New York', 'United States'], ['Roma', 'Italy']]
