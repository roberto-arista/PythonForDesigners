### Variables
radius = 30

### Instructions
newPage(592*2, 180)

# fill(.8)
# rect(0, 0, width(), height())

font('Arnold_v0.3-Regular', 18)
translate(70, height()*.55)
for angle in range(0, 360+1, 30):
    # the arcs
    stroke(0)
    strokeWidth(2)
    fill(None)
    newPath()
    arc((0, 0), radius, 0, angle, clockwise=False)
    drawPath()

    # center points + captions
    fill(0)
    stroke(None)
    oval(-2, -2, 4, 4)
    text(f'{angle}°', (0, -55), align='center')
    
    # moving forward
    translate(84.5, 0)
saveImage('arcs.png')
