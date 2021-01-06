#!/usr/bin/env python3

# -------------------------------- #
# Generate larger PNGs for the web #
# -------------------------------- #

# --- Modules --- #
import drawBot as dB
from pathlib import Path

# --- Constants --- #
SKIP = ['createPNGs.py', 'coloredCorners_FrederikALT.py', 'ambivalentSequence.py']

if __name__ == '__main__':
    # --- Variables --- #
    workingDir = Path('.')
    scalingFactor = 4

    # --- Instructions --- #
    scripts = [ff for ff in workingDir.iterdir()
               if ff.suffix == '.py' and ff.name not in SKIP]
    for eachPY in scripts:
        print(eachPY)
        dB.newDrawing()
        wdt, hgt = dB.imageSize(f'{eachPY.stem}.pdf')
        dB.newPage(wdt*scalingFactor, hgt*scalingFactor)
        dB.scale(scalingFactor)
        dB.image(f'{eachPY.stem}.pdf', (0, 0), pageNumber=1)
        print(f'{eachPY.stem}.png')
        # dB.saveImage(f'{eachPY.stem}.png')
        dB.endDrawing()
