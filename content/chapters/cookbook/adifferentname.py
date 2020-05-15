import csv

def loadTableWithKeys(filePath, delimiter, quotechar):
    table = []
    with open(filePath, mode='r', encoding='utf-8') as csvFile:
        tableReader = csv.reader(csvFile, delimiter=delimiter, quotechar=quotechar)
        for indexRow, eachRow in enumerate(tableReader):
            if indexRow == 0:
                keys = eachRow
            else:
                table.append({kk: vv for (kk, vv) in zip(keys, eachRow)})
    return table


if __name__ == '__main__':
    table = loadTableWithKeys('table.csv', '\t', '|')
    # [{'city': 'Shanghai', 'country': 'China'},
    #  {'city': 'New York', 'country': 'United States'},
    #  {'city': 'Roma', 'country': 'Italy'}]
