safetyLimit = 200    # this value is arbitrary
parachute = 0

while True:          # this will loop endlessly
    parachute += 1
    if parachute == safetyLimit:
        print("it's time to open the parachute")
        break