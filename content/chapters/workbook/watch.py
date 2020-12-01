#!/usr/bin/env python
# coding: utf-8

# ------------ #
# Draw a watch #
# ------------ #

# --- Modules --- #
from drawBot import stroke, fill, strokeWidth, oval, rotate, translate
from drawBot import save, restore, scale, size, width, height, line, saveImage
from datetime import datetime

### Constants
BLACK = (0, 0, 0)
RED = (1, 0, 0)
CIRCLE_ANGLE = 360

MAX_HOURS = 12
SECONDS_IN_MIN = MINUTES_IN_HOUR = 60

# --- Functions --- #
def shapeQualities(color=BLACK):
    stroke(None)
    fill(*color)

def lineQualities(thickness=1, color=BLACK):
    strokeWidth(thickness)
    stroke(*color)
    fill(None)

def drawWatch(watchRad, watchMargin,
              hourHandLen, hourHandTck, hourHandBar,
              minuteHandLen, minuteHandTck, minuteHandBar,
              secondHandLen, secondHandTck, secondHandBar, secondHandRad):

    save()    # main save/restore

    # outer oval
    lineQualities()
    oval(-watchRad, -watchRad, watchRad*2, watchRad*2)

    # draw numbers
    shapeQualities()
    for ii in range(MINUTES_IN_HOUR):

        save()
        angle = -ii*CIRCLE_ANGLE/MINUTES_IN_HOUR
        rotate(angle)
        translate(0, watchRad-watchMargin)

        if ii % 5 == 0:
            lineQualities(6)
            lineLength = 18
        else:
            lineQualities(1)
            lineLength = 6

        line((0, -lineLength), (0, 0))
        restore()

    # draw time
    justNow = datetime.now()

    # - start hour hand - #
    save()
    hourAngle = -(justNow.hour % MAX_HOURS)*CIRCLE_ANGLE/MAX_HOURS
    rotate(hourAngle)
    lineQualities(hourHandTck)
    line((0, -hourHandLen*hourHandBar), (0, hourHandLen*(1-hourHandBar)))
    restore()
    # - end hour hand - #

    # - start minute hand - #
    save()
    minuteAngle = -justNow.minute*CIRCLE_ANGLE/MINUTES_IN_HOUR
    rotate(minuteAngle)
    lineQualities(minuteHandTck)
    line((0, -minuteHandLen*minuteHandBar), (0, minuteHandLen*(1-minuteHandBar)))
    restore()
    # - end minute hand - #

    # - start second hand - #
    save()
    secondAngle = -justNow.second*CIRCLE_ANGLE/SECONDS_IN_MIN
    rotate(secondAngle)
    lineQualities(secondHandTck, RED)
    line((0, -secondHandLen*secondHandBar), (0, secondHandLen*(1-secondHandBar)))

    # big oval
    shapeQualities(RED)
    save()
    translate(0, secondHandLen*(1-secondHandBar))
    oval(-secondHandRad, -secondHandRad, secondHandRad*2, secondHandRad*2)
    restore()

    # small center oval
    save()
    scale(.6)
    oval(-secondHandRad, -secondHandRad, secondHandRad*2, secondHandRad*2)
    restore()

    restore()
    # - end second hand - #

    restore()    # main save/restore


# --- Instructions --- #
if __name__ == '__main__':
    size(200, 200)
    translate(width()/2, height()/2)
    drawWatch(watchRad=90, watchMargin=10,
              hourHandLen=76, hourHandTck=10, hourHandBar=.25,
              minuteHandLen=80, minuteHandTck=8, minuteHandBar=.15,
              secondHandLen=72, secondHandTck=2, secondHandBar=.3, secondHandRad=5)

    saveImage('watch.pdf')
