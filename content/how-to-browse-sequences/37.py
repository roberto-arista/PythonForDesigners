myRoute = [(10.2, 22.3, (7, 51, 43)),
           (12.6, 19.8, (7, 52, 2)),
           (14.5, 18.2, (7, 52, 54))
           ]

leading = 18
cellWidth = 50

size(200, 200)
font('InputMono-Regular')
fontSize(14)

for indexRow, eachRow in enumerate(myRoute):
    for indexCell, cellContent in enumerate(eachRow):
        x = indexCell*cellWidth
        y = height() - (indexRow+1)*leading

        if indexCell == 2:
            text('{:0>2}:{:0>2}:{:0>2}'.format(*cellContent), (x, y))
        else:
            text('{}'.format(cellContent), (x, y))