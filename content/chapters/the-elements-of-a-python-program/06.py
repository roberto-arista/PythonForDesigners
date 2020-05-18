def walk(distance, stepLength):
    walkedDistance = 0
    while distance > walkedDistance :
        oneStepForward(stepLength)
        walkedDistance += stepLength

walk(100, 5)