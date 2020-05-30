import csv

def loadTableWithKeys(filePath, delimiter, quotechar):
    with open(filePath, mode='r', encoding='utf-8') as csvFile:
        tableReader = csv.DictReader(csvFile, delimiter=delimiter, quotechar=quotechar)
        return list(tableReader)


if __name__ == '__main__':
    table = loadTableWithKeys('table.csv', '\t', '|')
    # [
    #     OrderedDict([('city', 'Shanghai'), ('country', 'China')]),
    #     OrderedDict([('city', 'New York'), ('country', 'United States')]),
    #     OrderedDict([('city', 'Roma'), ('country', 'Italy')])
    # ]
