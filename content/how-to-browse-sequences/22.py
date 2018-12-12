pages = 16
for eachPageNumber in range(1, pages+1):
    newPage(200, 200)
    fontSize(48)
    text(f'{eachPageNumber}', (20, 20))