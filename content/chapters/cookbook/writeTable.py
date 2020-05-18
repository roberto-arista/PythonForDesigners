import csv

def writeTable(data, fileName, delimiter):
    with open(fileName, mode='w', encoding='utf-8') as csvFile:
        tableWriter = csv.writer(csvFile, delimiter='\t')
        tableWriter.writerows(data)


if __name__ == '__main__':
    data = [
        ('city', 'country'),
        ('Shanghai', 'China'),
        ('New York', 'United States'),
        ('Roma', 'Italy')
    ]
    writeTable(data, 'table.csv', delimiter='\t')
