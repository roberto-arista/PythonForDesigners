WHITE = 1, 1, 1

def background(clr=WHITE):
    fill(*clr)
    rect(0, 0, width(), height())

if __name__ == '__main__':
    newPage(400, 400)
    pink = 255/255, 51/255, 102/255
    background(clr=pink)
