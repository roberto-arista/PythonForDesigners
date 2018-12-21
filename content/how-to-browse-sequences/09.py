someCoordinates = [(11.2, 32.1),
                   (43.9, 14.8)]

firstPoint = (34.1, 76.4)
someCoordinates.insert(0, firstPoint)
# result: [(34.1, 76.4), (11.2, 32.1), (43.9, 14.8)]
lastPoint = (63.1, 87.3)
someCoordinates.insert(len(someCoordinates), lastPoint)
# result: [(34.1, 76.4), (11.2, 32.1), (43.9, 14.8), (63.1, 87.3)]
aPoint = (87.4, 6.2)
someCoordinates.insert(2, aPoint)
# result: [(34.1, 76.4), (11.2, 32.1), (87.4, 6.2), (43.9, 14.8), (63.1, 87.3)]
anotherPoint = (45.9, 98.7)
someCoordinates.insert(200, anotherPoint)
# result: [(34.1, 76.4), (11.2, 32.1), (87.4, 6.2), (43.9, 14.8), (63.1, 87.3), (45.9, 98.7)]
# insert does not complain if the index is way bigger than the list
# it will put the element at the end of the list without raising an IndexError