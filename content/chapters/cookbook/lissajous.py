from math import pi, sin

def calcLissajous(ptsAmount, amps, angFreqs, angPhases):
    ampX, ampY = amps
    angFreqX, angFreqY = angFreqs
    angPhaseX, angPhaseY = angPhases
    points = []
    for ii in range(0, ptsAmount):
        tt = ii*pi*2/ptsAmount
        xx = ampX * sin(angFreqX * tt + angPhaseX)
        yy = ampY * sin(angFreqY * tt + angPhaseY)
        points.append((xx, yy))
    return points


if __name__ == '__main__':
    pointsAmount = 500

    ampX = ampY = 200
    angFreqX = 3
    angFreqY = 1
    angPhaseX = pi
    angPhaseY = pi/2

    lissajousPoints = calcLissajous(pointsAmount, (ampX, ampY), (angFreqX, angFreqY), (angPhaseX, angPhaseY))
    newPage(500, 500)
    translate(width()/2, height()/2)
    stroke(0)
    strokeWidth(10)
    fill(None)
    polygon(*lissajousPoints)
